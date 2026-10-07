from pathlib import Path
import re
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SOURCE = Path("results/newsource_final/per_eval.csv")
OUT = Path("results/newsource_final/curves")
OUT.mkdir(parents=True, exist_ok=True)

raw = pd.read_csv(SOURCE)

def find_col(candidates, required=True):
    def norm(s):
        return re.sub(r"[^a-z0-9]", "", s.lower())

    available = {norm(c): c for c in raw.columns}
    for candidate in candidates:
        if norm(candidate) in available:
            return available[norm(candidate)]

    if required:
        raise ValueError(
            f"Δεν βρέθηκε στήλη {candidates}. "
            f"Διαθέσιμες: {list(raw.columns)}"
        )
    return None

run_col = find_col(["run", "run_name", "experiment"])
ap_col = find_col(["AP50", "bbox_AP50", "det_AP50"])
seg_col = find_col(["mIoU", "sem_seg_mIoU"])
dataset_col = find_col(
    ["dataset", "dataset_name", "eval_dataset",
     "corruption", "domain"],
    required=False
)
index_col = find_col(
    ["eval_idx", "eval_index", "evaluation_index",
     "eval_num", "eval_number"],
    required=False
)

protocols = {
    "ACDC": {
        "stem": "acdcLT",
        "domains": ["fog", "night", "rain", "snow"]
    },
    "CSC": {
        "stem": "cscLT",
        "domains": [
            "fog", "motion_blur", "snow",
            "brightness", "defocus_blur"
        ]
    }
}

variants = {
    "Base": "base",
    "CT-CL": "ctcl",
    "CT-CR": "ctcr",
    "CT-CL+CT-CR": "ctcl_ctcr",
    "+CTPV": "ctcl_ctcr_ctpv"
}

all_evals = []

for dataset, cfg in protocols.items():
    domains = cfg["domains"]
    expected = len(domains) * 10

    for variant, stem in variants.items():
        run = f"newsrc_{stem}_{cfg['stem']}_s0"

        d = raw.loc[raw[run_col] == run].copy()

        if len(d) != expected:
            raise ValueError(
                f"{run}: βρέθηκαν {len(d)}/{expected} "
                "evaluations. Ελέγξτε το per_eval.csv."
            )

        # Χρησιμοποιούμε το evaluation index όπου υπάρχει.
        if index_col:
            numeric_idx = pd.to_numeric(
                d[index_col], errors="coerce"
            )
            if numeric_idx.notna().all() and numeric_idx.is_unique:
                d = d.assign(_idx=numeric_idx).sort_values("_idx")

        d = d.reset_index(drop=True)

        expected_domains = domains * 10

        # Επαλήθευση ότι οι ετικέτες των datasets
        # συμφωνούν με την πραγματική σειρά του stream.
        if dataset_col:
            for i, expected_domain in enumerate(expected_domains):
                actual = str(d.loc[i, dataset_col]).lower()
                if expected_domain not in actual:
                    raise ValueError(
                        f"{run}, evaluation {i+1}: "
                        f"αναμενόταν {expected_domain}, "
                        f"αλλά το CSV γράφει {actual}. "
                        "Ελέγξτε τη σειρά πριν σχεδιάσετε."
                    )
        else:
            print(
                f"ΠΡΟΣΟΧΗ: Δεν υπάρχει στήλη dataset. "
                f"Χρησιμοποιείται η γνωστή σειρά για {run}."
            )

        result = pd.DataFrame({
            "run": run,
            "dataset": dataset,
            "variant": variant,
            "eval": np.arange(1, expected + 1),
            "round": np.arange(expected) // len(domains) + 1,
            "domain": expected_domains,
            "AP50": pd.to_numeric(
                d[ap_col], errors="coerce"
            ).to_numpy(),
            "mIoU": pd.to_numeric(
                d[seg_col], errors="coerce"
            ).to_numpy()
        })

        if result[["AP50", "mIoU"]].isna().any().any():
            raise ValueError(f"{run}: λείπουν AP50 ή mIoU.")

        all_evals.append(result)

ev = pd.concat(all_evals, ignore_index=True)

# Μέσοι όροι ανά round και ανά corruption/round.
rounds = (
    ev.groupby(["dataset", "variant", "round"], as_index=False)
      [["AP50", "mIoU"]].mean()
)

domain_rounds = (
    ev.groupby(
        ["dataset", "variant", "domain", "round"],
        as_index=False
    )[["AP50", "mIoU"]].mean()
)

ev.to_csv(OUT / "selected_evaluations.csv", index=False)
rounds.to_csv(OUT / "round_means.csv", index=False)
domain_rounds.to_csv(OUT / "domain_round_means.csv", index=False)

for dataset, cfg in protocols.items():
    for metric in ["AP50", "mIoU"]:

        # Γράφημα 1: όλα τα variants, μέση τιμή ανά round.
        fig, ax = plt.subplots(figsize=(10, 5.5))

        for variant in variants:
            d = rounds[
                (rounds.dataset == dataset) &
                (rounds.variant == variant)
            ].sort_values("round")

            ax.plot(
                d["round"], d[metric],
                marker="o", label=variant
            )

        ax.set(
            title=f"{dataset}-LT: {metric} ανά round",
            xlabel="Round",
            ylabel=metric,
            xticks=range(1, 11)
        )
        ax.grid(alpha=0.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(
            OUT / f"{dataset}_{metric}_rounds.png",
            dpi=180
        )
        plt.close(fig)

        # Γράφημα 2: κάθε corruption ξεχωριστά,
        # αρχικά μόνο για Base και CT-CR.
        for variant in ["Base", "CT-CR"]:
            fig, ax = plt.subplots(figsize=(10, 5.5))

            for domain in cfg["domains"]:
                d = domain_rounds[
                    (domain_rounds.dataset == dataset) &
                    (domain_rounds.variant == variant) &
                    (domain_rounds.domain == domain)
                ].sort_values("round")

                ax.plot(
                    d["round"], d[metric],
                    marker="o", label=domain
                )

            ax.set(
                title=f"{dataset}: {variant} — {metric}",
                xlabel="Round",
                ylabel=metric,
                xticks=range(1, 11)
            )
            ax.grid(alpha=0.3)
            ax.legend()
            fig.tight_layout()

            safe_variant = variant.replace("-", "")
            fig.savefig(
                OUT / f"{dataset}_{safe_variant}_{metric}_domains.png",
                dpi=180
            )
            plt.close(fig)

print("\nΟλοκληρώθηκε η εξαγωγή.")
print(f"Evaluations: {len(ev)}")
print(f"Αποτελέσματα: {OUT}")
print("\nΠρώτο και τελευταίο round:")
print(
    rounds[rounds["round"].isin([1, 10])]
    .sort_values(["dataset", "variant", "round"])
    .to_string(index=False)
)
