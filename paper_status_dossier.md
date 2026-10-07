# PAPER STATUS DOSSIER
## Joint Continual Test-Time Adaptation for Object Detection + Semantic Segmentation

### Purpose
This compact dossier is for an independent paper-readiness audit. The goal is **not** to propose more ablations by default, but to decide:
1. what the strongest defensible paper contribution already is,
2. whether a new adaptive mechanism is actually necessary,
3. what the minimum remaining experiments are before writing/submission.

---

## 1. Problem setting

We study **source-free online continual test-time adaptation (CTTA)** for **joint object detection (OD) + semantic segmentation (SemSeg)** using a **single shared multitask Panoptic-FPN R50 model**.

The model is trained on Cityscapes and adapted online without source data during target-stream inference.

Main target streams:

### ACDC-LT ×10
`fog → night → rain → snow`, repeated 10 times, no reset.

### Cityscapes-C mixed LT ×10
`fog → motion_blur → snow → brightness → defocus_blur`, repeated 10 times, no reset.

Metrics:
- OD: AP50
- SemSeg: mIoU

Important comparisons use the **same source checkpoint**.

---

## 2. Current architecture / method family

The framework extends an AMROD-style CTTA setup to a multitask Panoptic-FPN model.

Main components explored:
- teacher/student/anchor CTTA,
- OD pseudo-label adaptation,
- semantic self-training,
- CT-CR cross-task regularization,
- gradient-routing / negative-transfer mechanisms,
- Task-CoCo gradient consensus,
- frozen-teacher retention diagnostics.

A key routing mechanism is `resnet_route`.

Static routing:

**ResNet bottom-up**
`g = g_det + λ * g_aux`

**FPN + task heads**
`g = g_det + g_aux`

where `g_aux` aggregates non-detection objectives in the current implementation.

---

## 3. Static shared-plasticity sweep

Full long-term seed-0 results:

| λ | ACDC AP50 | ACDC mIoU | CSC AP50 | CSC mIoU |
|---:|---:|---:|---:|---:|
| 0.00 | 43.2709 | 40.1040 | **27.8585** | **34.2901** |
| 0.25 | 43.1924 | 40.7366 | 27.2180 | 34.0730 |
| 0.50 | 43.2616 | 40.7142 | 26.4556 | 33.5634 |
| 1.00 | **43.8807** | **41.8170** | 27.0794 | 33.1045 |

Key empirical result:
- **ACDC prefers high shared-ResNet plasticity (`λ≈1`)**
- **CSC prefers strong ResNet protection (`λ≈0`)**

Therefore there is **no globally optimal static shared-backbone plasticity level** across the two streams.

---

## 4. Task-CoCo experiment

Task-CoCo was implemented as task-level Gradient Consensus between:
- `g_det`
- `g_seg`

Important design details:
- CT-CR and other regularizers were kept separate and unchanged.
- CoCo was applied only to shared parameters.
- The separate CoCo Plasticity Constraint was **not** implemented in this experiment.

Full LT results:

| Method | ACDC AP50 | ACDC mIoU | CSC AP50 | CSC mIoU |
|---|---:|---:|---:|---:|
| Task-CoCo | 43.5145 | 41.3939 | 26.0045 | 32.4874 |

Interpretation:
- Task-CoCo is reasonable on ACDC.
- It performs poorly on CSC, especially long-term segmentation.
- **Instantaneous task-gradient consensus does not solve the observed long-term retention problem.**

CSC Task-CoCo:
- R1 mIoU: 31.2983
- peak mIoU: 33.6552 at R3
- R10 mIoU: 31.1460
- peak→R10 drop: -2.5092

---

## 5. Reproduced task-specific baselines

Same-source reproduced baselines include:

### Detection
AMROD:
- ACDC-LT AP50 ≈ 38.744
- CSC-LT AP50 ≈ 26.149

### Semantic segmentation
TENT:
- ACDC-LT mIoU ≈ 35.469
- CSC-LT mIoU ≈ 27.781

CoTTA:
- ACDC-LT mIoU ≈ 20.600
- CSC-LT mIoU ≈ 26.731

Important:
- missing metrics are not treated as zero,
- these baselines are task-specific rather than joint OD+SemSeg methods.

The current multitask variants are therefore already very competitive against these same-source reproduced task-specific CTTA baselines.

---

## 6. Retention diagnostics

A frozen-teacher retention probe was implemented.

The probe evaluates the current teacher **without adaptation**, so probing does not advance model iteration or alter the CTTA state.

### 6.1 Pairwise interference

Protocol:
1. adapt on fog,
2. frozen probe on fog,
3. adapt on one challenger,
4. frozen probe on fog again.

Challengers:
- motion blur
- snow
- brightness
- defocus blur

Result:
**all isolated fog→challenger transitions were neutral or positive**.

Mean pairwise fog ΔmIoU:
- Base: +0.53
- λ=0: +1.43
- λ=1: +0.88
- Task-CoCo: +0.91

Therefore the failure is **not explained by one intrinsically destructive domain transition**.

---

## 7. Longitudinal retention

CSC cycle:
`fog → motion → snow → brightness → defocus`, repeated 3 rounds.

Frozen fog is probed after every adaptation domain.

Fog mIoU change from immediately after fog to end of the same round:

| Method | R1 | R2 | R3 |
|---|---:|---:|---:|
| Base | -0.530 | -0.613 | -0.602 |
| λ=0 | +2.427 | -0.606 | -0.863 |
| λ=1 | +0.423 | -1.026 | -1.824 |
| Task-CoCo | +0.365 | -0.671 | -1.611 |

Key result:
**the same cycle becomes progressively more destructive with adaptation history**.

Cumulative frozen fog mIoU, R1-after-fog → R3-end:
- Base: -0.474
- λ=0: **+2.201**
- λ=1: -1.120
- Task-CoCo: -0.851

Frozen 5-domain mean at end of R3:

| Method | AP50 | mIoU |
|---|---:|---:|
| Base | 24.017 | 33.882 |
| λ=0 | **27.304** | **35.627** |
| λ=1 | 26.317 | 34.457 |
| Task-CoCo | 24.656 | 33.785 |

Interpretation:
- CSC benefits strongly from protecting the ResNet representation.
- The problem is **history-dependent cumulative interference / drift**, not merely instantaneous task-gradient conflict.

---

## 8. Adaptive source-anchor routing diagnostic

An existing binary adaptive-routing baseline was tested.

Signal:
teacher-vs-frozen-source-anchor semantic agreement EMA relative to all-time running maximum.

Rule:
- open: `λ=1`
- closed: `λ=0`

### CSC
- open: 0.7%
- closed: 99.3%
- final agreement / peak ratio ≈ 0.777

The router effectively collapses to static `λ=0`.

R3 frozen 5-domain mean:
- AP50 ≈ 27.830
- mIoU ≈ 35.838

This is slightly above static λ=0 in the 3-round diagnostic, but almost all adaptation steps are closed, so it is not genuinely adaptive.

### ACDC
- open: 2.1%
- closed: 97.9%
- final agreement / peak ratio ≈ 0.850

Yet frozen fog retention **improves**:

- R1: 46.669 → 48.644 (+1.975)
- R2: 49.103 → 49.651 (+0.549)
- R3: 49.920 → 49.997 (+0.077)

Round-end ACDC frozen means:

| Round | AP50 | mIoU |
|---|---:|---:|
| R1 | 39.729 | 38.896 |
| R2 | 41.769 | 40.019 |
| R3 | 43.058 | 40.606 |

Key conclusion:
**distance from the source anchor is not equivalent to harmful forgetting.**

The binary source-relative router closes almost everywhere on both streams, although ACDC clearly still benefits from adaptation.

Therefore:
- absolute source-anchor agreement is not sufficient as the sole plasticity-control signal,
- history-relative / representation-level / task-specific stability measures may be more appropriate.

---

## 9. Current scientific story

The strongest evidence currently supports:

1. Joint OD+SemSeg CTTA has a distinct **shared-plasticity problem**.
2. A single static degree of shared-backbone adaptation is not optimal across target streams.
3. Instantaneous gradient-conflict resolution alone does not solve long-term retention.
4. Pairwise domain transitions are mostly benign.
5. Negative transfer emerges **with continual history**.
6. Protecting the shared ResNet representation can substantially improve CSC retention.
7. Simply staying close to the frozen source anchor is not the right objective:
   ACDC can drift away from source while retention improves.

Potential framing:

> **Multi-task CTTA requires distinguishing productive adaptation from destructive history-dependent drift in the shared representation.**

---

## 10. Is a new mechanism required?

This is intentionally unresolved.

### Direction A — no new complex mechanism
Position the contribution around:
- joint OD+SemSeg CTTA,
- same-source benchmarking,
- strong multitask results,
- negative-transfer / shared-plasticity analysis,
- static ResNet routing as a simple effective intervention,
- retention diagnostics showing why existing gradient/source-relative strategies fail.

This would be an analysis + strong-method paper.

### Direction B — one final history-aware plasticity mechanism
Add exactly one final mechanism only if it clearly improves the paper:
- history-relative,
- label-free,
- domain-agnostic if possible,
- task- or layer-specific,
- experimentally falsifiable,
- minimal added complexity.

No further broad ablation program should be started without a clear reviewer-facing reason.

---

## 11. Recent literature to inspect

Prioritize **2025–2026** work and do not rely mainly on older CL/MTL ideas.

Must inspect supplied PDFs for:
- CoCo-MT-TTA, AAAI 2026 — especially Plasticity Constraint
- ConsMTL, CVPR 2025
- PIVRG / Revisiting Fairness in Multitask Learning, CVPR 2025
- MMTL-UniAD, CVPR 2025
- TADFormer, CVPR 2025
- CORE-MTL, ICML 2026
- MoASE / MoASE++, 2026
- directly relevant IEEE / Springer 2025–2026 papers on:
  - multi-task learning,
  - CTTA/TTA,
  - stability–plasticity,
  - shared/task-specific parameter control,
  - autonomous-driving multi-task perception.

Do not treat a paper as relevant merely because it is recent.

---

## 12. Paper-readiness audit questions

Please answer critically:

1. What is the strongest defensible paper contribution **with the results already available**?
2. Is a new adaptive/history-aware mechanism truly necessary for publication, or is it scope creep?
3. Which claims are already supported?
4. Which claims are not yet sufficiently supported?
5. What are the 3–5 most likely reviewer objections?
6. What is the **minimum remaining experiment set** before writing/submission?
7. Which experiments/ablations should be stopped because they no longer strengthen the paper?
8. What should be:
   - the main result table,
   - the main ablation table,
   - the key diagnostic figure?
9. Which recent methods absolutely need to appear as baselines or discussion?
10. Propose two paper framings:
    - without adding a new mechanism,
    - with one final history-aware plasticity mechanism.
11. Recommend a concrete stopping rule: after which experiments should implementation end and manuscript writing begin?

Be critical. Prefer scientific completeness and a short route to submission over additional complexity.
