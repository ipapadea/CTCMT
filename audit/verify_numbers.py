"""Recompute the slide numbers from raw run logs and print the resolved config.

Usage:
    python verify_numbers.py /path/to/amrod_output/ctta_acdc [/path/to/amrod_output/logs]

Needs only PyYAML. Reads <run>/config.yaml and <run>/log.txt (detectron2 log).
The optional second argument enables the stdout-trace checks (gate / aug-avg).
"""
import os
import re
import statistics as st
import sys

import yaml

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
LOGS = sys.argv[2] if len(sys.argv) > 2 else None

KEYS = [
    "CTCMT_CONFLICT_MODE", "CTCMT_AUX_TRUNK_LAMBDA", "CTCMT_WEIGHT_CTCR", "CTCMT_CTCR_MODE",
    "CTCMT_WEIGHT_CTCL", "CTCMT_CTCL_ENABLED", "CTCMT_CTPV_ENABLED",
    "CTCMT_ANCHOR_MARGINAL_WEIGHT", "CTCMT_CLASS_BALANCED_CE", "CTCMT_SEG_LOSS_SCALE_PRESERVE",
    "CTCMT_STRONG_AUG_STUDENT", "CTCMT_SEG_AUG_ENABLED", "CTCMT_CROSS_TASK_FISHER",
    "CTCMT_BACKBONE_RST_FACTOR", "RST_M", "MT", "THRESHOLD_MAX", "SCORE_THRESH",
    "CTCMT_DET_ONLY", "CTCMT_SEG_ONLY",
]


def metrics(run):
    """Mean AP50 (bbox) and mean mIoU over all evaluation rounds of a run."""
    lines = open(os.path.join(ROOT, run, "log.txt"), errors="ignore").read().split("\n")
    ap50 = [float(lines[i + 2].split("copypaste: ")[1].split(",")[1])
            for i, l in enumerate(lines) if "copypaste: Task: bbox" in l]
    miou = [float(x) for x in re.findall(r"'mIoU': ([0-9.]+)", "\n".join(lines))]
    mean = lambda x: sum(x) / len(x) if x else float("nan")
    return mean(ap50), mean(miou), len(ap50), len(miou)


def cfg(run):
    c = yaml.safe_load(open(os.path.join(ROOT, run, "config.yaml")))
    return c["MODEL"]["META_ARCHITECTURE"], {k.replace("CTCMT_", ""): c["SOLVER"].get(k) for k in KEYS}


def group(title, runs):
    vals = [metrics(r) for r in runs if os.path.isdir(os.path.join(ROOT, r))]
    if not vals:
        print(f"{title:55s} (no runs found)")
        return
    ap, mi = [v[0] for v in vals], [v[1] for v in vals]
    sd = lambda x: st.stdev(x) if len(x) > 1 else 0.0
    print(f"{title:55s} n={len(vals)}  AP50 {st.mean(ap):7.3f} +- {sd(ap):.3f}   mIoU {st.mean(mi):7.3f} +- {sd(mi):.3f}")


S = ("0", "42", "123")
print("== Slides 20-21 (3-seed means; compare with tables) ==")
group("CTCMT ACDC4", [f"headline_lam1_acdc4_s{s}" for s in S])
group("CTCMT CSC12", [f"headline_lam1_csc12_s{s}" for s in S])
group("CTCMT ACDC-LT", ["newsrc_lam1_acdcLT_s0_explicit", "newsrc_lam1_acdcLT_s42", "newsrc_lam1_acdcLT_s123"])
group("CTCMT CSC-LT", ["newsrc_lam1_cscLT_s0_explicit", "newsrc_lam1_cscLT_s42", "newsrc_lam1_cscLT_s123"])
group("Base ACDC4", [f"paper_base_acdc4_s{s}" for s in S])
group("Base CSC12", [f"paper_base_csc12_s{s}" for s in S])
group("Base ACDC-LT", ["newsrc_base_acdcLT_s0", "paper_base_acdcLT_s42", "paper_base_acdcLT_s123"])
group("Base CSC-LT", ["newsrc_base_cscLT_s0", "paper_base_cscLT_s42", "paper_base_cscLT_s123"])
group("CT-CR+Task-CoCo ACDC4", ["newsrc_taskcoco_acdcLT_s0", "paper_taskcoco_acdc4_s42", "paper_taskcoco_acdc4_s123"])
group("CT-CR+Task-CoCo CSC12", [f"paper_taskcoco_csc12_s{s}" for s in S])
group("CT-CR+Task-CoCo ACDC-LT", ["newsrc_taskcoco_acdcLT10_s0", "paper_taskcoco_acdcLT_s42", "paper_taskcoco_acdcLT_s123"])
group("CT-CR+Task-CoCo CSC-LT", ["newsrc_taskcoco_cscLT_s0", "paper_taskcoco_cscLT_s42", "paper_taskcoco_cscLT_s123"])

print("\n== Slide 12 (CSC12 ablation) ==")
for v in ("base", "ctcr", "ctcl", "both", "all"):
    group(f"ablate {v}", [f"paper26_ablate_csc12_{v}_s{s}" for s in S])

print("\n== Slide 16 (seed 0) ==")
for w in ("0p0", "0p1", "0p3", "0p5", "1p0"):
    for ds in ("csc12", "acdc4"):
        group(f"weight {w} {ds}", [f"paper26_weight_{ds}_w{w}_s0"])
for o in ("canonical", "reverse", "random2026"):
    for k in ("base", "ours"):
        group(f"order {o} {k}", [f"paper26_order_csc12_{o}_{k}_s0"])

print("\n== Slides 13/15 (OLD source checkpoint, CSC-LT) ==")
group("Full MTL e13a (CT-CL 0.5 + CT-CR 0.3), seed 0", ["e13a_thrmax080_cscLT_s0"])
group("DET-only e15, seed 0", ["e15_detonly_thr080_cscLT_s0"])
group("DET-only e15, 3 seeds", [f"e15_detonly_thr080_cscLT_s{s}" for s in S])
group("SEG-only e21, seed 0", ["e21_segonly_thr080_cscLT_s0"])
group("Routed SEG e22 (aux_head_only), 3 seeds", [f"e22_seghead_only_cscLT_s{s}" for s in S])

print("\n== Restore diagnostic (seed 0) ==")
group("headline ACDC4 (restore on)", ["headline_lam1_acdc4_s0"])
group("no restore ACDC4", ["paper26_fisher_norestore_acdc4_s0"])
group("headline CSC12 (restore on)", ["headline_lam1_csc12_s0"])
group("no restore CSC12", ["paper26_fisher_norestore_csc12_s0"])

print("\n== Resolved key config of representative runs ==")
for r in ("headline_lam1_acdc4_s0", "headline_lam1_csc12_s0", "paper_base_acdc4_s0",
          "paper_taskcoco_acdc4_s42", "e13a_thrmax080_cscLT_s0", "e22_seghead_only_cscLT_s0"):
    if os.path.isdir(os.path.join(ROOT, r)):
        print(r, cfg(r))

if LOGS:
    print("\n== Stdout traces: gate behaviour and aug-avg firing rate ==")
    traces = ["headline_lam1_acdc4_s0.log", "headline_lam1_csc12_s0.log",
              "batch_lam1_acdcLT_s0_explicit.out", "batch_lam1_cscLT_s0_explicit.out"]
    for t in traces:
        p = os.path.join(LOGS, t)
        if not os.path.exists(p):
            continue
        L = [l for l in open(p, errors="ignore") if "CT-CMT-MTL] iter" in l]
        det_absent = [l for l in L if "det/loss_cls" not in l]
        closed = [l for l in det_absent if "n_pseudo=0" not in l]
        ok = all("seg/soft_ce" in l and "seg/anchor_marginal" in l and " ctcr=" in l for l in closed)
        m = re.search(r"segaug=(\d+)/(\d+)", L[-1])
        print(f"{t}: prints={len(L)} gate-closed-with-pseudo-boxes={len(closed)} "
              f"seg+anchor+ctcr present in all of them={ok} "
              f"segaug fired={int(m.group(1))}/{int(m.group(2))} ({int(m.group(1)) / int(m.group(2)):.3f})")
