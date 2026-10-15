# CTCMT slides vs. code: technical audit

Audited deck: `CTCMT_lab_meeting_simple_v7.tex` (slides 5-25; slides 1-4 read for context) and
`file_slides_final_tables_v2.tex` (result tables).
Rule: executable code is ground truth. Where the deck disagrees with the code, the deck changes.
No code change is proposed.

## 0. How to read this pack

| File | What it is |
|---|---|
| `ctcmt_mtl.py` | The method. Identical (byte-for-byte) to commit `be9771c`, the code that produced the headline runs. **Line numbers in this document refer to this file** unless stated otherwise. |
| `ctcmt_mtl_with_fisher_30647ff.py` | Same file at HEAD `30647ff`. It adds the experimental Fisher variants (all default OFF). Needed only to check slide 17. |
| `defaults.py` | Config defaults (`SOLVER.CTCMT_*`) at `be9771c`. |
| `configs/*.yaml` | Fully resolved `config.yaml` of representative runs (no `_BASE_` chain). |
| `verify_numbers.py`, `verify_output.txt` | Recomputes every slide number from raw run logs. The output is saved. |
| `*.tex` | The two audited decks. |

There is no `ctcmt/ctta/*` package. The whole method is the single class `CTCMT_MTL`
in `detectron2/detectron2/modeling/meta_arch/ctcmt_mtl.py`.
The evaluation entry point is `detectron2/tools/train_net.py --eval-only` (see section 1, item 10).

### Experiment to slide mapping (verified by `verify_numbers.py`)

| Slides | Runs (under `amrod_output/ctta_acdc/`) | Result |
|---|---|---|
| 20-21 CTCMT | short: `headline_lam1_{acdc4,csc12}_s{0,42,123}`; long: `newsrc_lam1_{acdcLT,cscLT}_s0_explicit`, `_s42`, `_s123` | All 8 means match the tables, e.g. 38.007 / 17.722 / 44.076 / 26.725 AP50. |
| 20-21 Base | `paper_base_*`, `newsrc_base_*_s0` | All 8 means match, e.g. 36.839 / 16.957 / 42.494 / 25.266. |
| 20-21 CT-CR+Task-CoCo | `paper_taskcoco_*`, `newsrc_taskcoco_*_s0` | All 8 means match, e.g. 37.749. |
| 12 | `paper26_ablate_csc12_{base,ctcr,ctcl,both,all}_s{0,42,123}` | All 10 values match. |
| 16 | `paper26_weight_*`, `paper26_order_csc12_*` | Match. The ACDC4 run with λ=1.0 gives NaN AP50. |
| 13, 15 | `e13a_*`, `e15_*`, `e21_*`, `e22_*` (old source `panoptic_fpn_R50_cityscapes`, CSC-LT) | Numbers match. The arm contents differ from the slide text (see slides 13 and 15). |
| 23 | `scripts/paper26_batch_efficiency.sh` -> `efficiency_summary_all.json` | ms/FPS match. 400 measured frames after 50 warm-up, 3 repeats, `defocus_blur_mtl`. |

### What the executed headline config is

Identical in `headline_lam1_*` and `newsrc_lam1_*` (see `configs/`):

- `CTCR_MODE=soft_seg_global`, `WEIGHT_CTCR=0.3`, `CTCR_WEIGHT_FLOOR=0.2`.
- `WEIGHT_DET=1`, `WEIGHT_SEG=1`, `ANCHOR_MARGINAL_WEIGHT=0.1`.
- `CLASS_BALANCED_CE` (beta 0.5, marginal EMA 0.999), `SEG_LOSS_SCALE_PRESERVE`.
- `STRONG_AUG_STUDENT`, `SEG_AUG_ENABLED` (conf thresh 0.95, scales (0.75, 1.0, 1.25), flips (False, True)).
- `MT=0.9998`, `RST_M=0.01`, `CROSS_TASK_FISHER=True` (historical name; see 1.9), `BACKBONE_RST_FACTOR=0.1`.
- `SCORE_EM=0.5`, `SCORE_GAMMA=0.7`, `SCORE_THRESH=1.4`.
- `THRESHOLD_INIT=0.8`, `THRESHOLD_MINI=0.7`, `ALPHA_DT=1.3`, `GAMMA_DT=0.95`.
- `THRESHOLD_MAX=0.9` on ACDC and `0.8` on Cityscapes-C.
- SGD lr 1e-3, momentum 0.9, weight decay 1e-4, batch size 1.
- `CTCL_ENABLED=False`, `CTPV_ENABLED=False`, no det/seg-only, no Fisher, no per-task or directional gate.
- `CONFLICT_MODE=resnet_route` with `AUX_TRUNK_LAMBDA=1.0`. At lambda=1 the combined gradient equals `g_det + g_aux`
  (`_backward_and_combine`), i.e. ordinary joint backprop. The mode only adds a second backward pass.

**Base** differs from the headline config only in `WEIGHT_CTCR=0` and `CONFLICT_MODE=none`.
It still has strong-aug student, class balancing, anchor KL, aug-averaging, gating and restore.

**Code stability check.** `git diff 4b09d55..HEAD` on `ctcmt_mtl.py` shows no change to the default paths
(`_teacher_pseudo`, `_dyn_thresholds`, `_ctcr_loss` soft_seg_global, seg loss, `_ctpv_filter`, `_ctcl_loss`, EMA, restore).
Later additions are flag-gated (routing, Task-CoCo, Fisher) or diagnostics.
The old runs `e13a`..`e22` (8-11 Sep) ran on a working tree that was committed later as `4b09d55`.
Their configs and that commit agree, but byte-identity cannot be proven.

**Empirical confirmation from stdout traces** (`verify_output.txt`, last section).
Each 50 frames the model prints the losses of the current frame.
- In every printed frame where the det loss is absent but pseudo-boxes exist (gate closed), `seg/soft_ce`,
  `seg/anchor_marginal` and `ctcr` are present (3/3, 11/11, 66/66, 36/36 over four runs).
- The seg aug-averaging fires on 96.8-99.4% of frames.
- The printed max threshold is 0.900 (ACDC) and 0.800 (CSC), so the cap binds in practice.

## 1. Canonical CTCMT according to the code

All locations refer to `ctcmt_mtl.py` (`be9771c` line numbers).

### 1. Algorithm flow, `CTCMT_MTL.forward` (l.2067)
Per frame (batch size 1):
1. `_teacher_pseudo` (l.625): teacher inference on the weak view (no grad), dynamic per-class thresholds, score-EMA gate.
2. CTPV filter, only if enabled (off in CTCMT).
3. Student forward on the **strong** view (`image_strong`).
4. Losses (see 2-7), one backward, one SGD step.
5. `_update_teacher` (EMA), then `_stochastic_restore` (student toward source).
6. Final prediction: a second `teacher.inference` on the **weak** view, **after** the update. This is adapt-then-predict with the EMA teacher.
   The teacher runs twice per frame; the pseudo-labels come from the pre-update teacher.

### 2. L_det
`forward`, branch "Det consistency". Applied only if `not seg_only and det_gate and len(pseudo_inst)>0`.
Standard `proposal_generator` and `roi_heads` losses of the student (`loss_rpn_cls`, `loss_rpn_loc`, `loss_cls`, `loss_box_reg`, weight 1.0).
The targets are hard pseudo ground truth (`_to_gt_instances`, l.708): teacher boxes and classes after NMS 0.5, score >= 0.05 and per-class thresholds.
There is no soft consistency.

Dynamic thresholds (`_dyn_thresholds`, l.138; called from `_teacher_pseudo`):
- `s_bar_c` = mean score of class c among detections with score > 0.1 (hard-coded floor).
- If class c has such detections: `tau_c = clip_[0.7, tau_max](0.95*tau_c + 0.05*1.3*sqrt(s_bar_c))`.
- If class c has none: `tau_c` is unchanged (re-clipped only).
- `tau_c` starts at 0.8.
- It is updated even when the gate is closed.
- It is not updated when the teacher has no detection with score > 0.1.

### 3. L_seg
`forward`, branch "Sem-seg soft-CE" (not det-only, `seg_gate`):
- `l_i = -sum_k q_T[i,k] * log p_S[i,k]`. This is soft cross-entropy, not hard CE and not entropy minimisation.
- Class balancing (`CLASS_BALANCED_CE`): running EMA (0.999) of the teacher class marginal `m` (`_update_class_marginal`, l.1052),
  `w = m[argmax q_T]^-0.5`, normalised to mean 1.
- `L_cb = sum(w*l) / (sum(w) + 1e-6)`.
- `L_seg = kappa * L_cb` with `kappa = stopgrad(mean(l) / L_cb)` (`SEG_LOSS_SCALE_PRESERVE`).
- No entropy weighting. No pixel-wise anchor loss.
- Anchor term, `seg/anchor_marginal`: `0.1 * KL(q_A || q_S) = 0.1 * sum_k q_A[k] (log q_A[k] - log q_S[k])`.
  `q_A` and `q_S` are image-level mean softmax class marginals of the frozen anchor (no grad) and the student.
  The anchor sees the strong image.
- `q_T` (conditional aug-averaging):
  - Trigger: the mean pixelwise max-prob of the **frozen anchor** is < 0.95.
  - If triggered, `q_T` is the **teacher** softmax averaged over scales {0.75, 1.0, 1.25} x flips {off, on}
    (`_teacher_aug_avg_seg_probs`, l.2037), computed on the **student's strong image tensor**.
  - Otherwise `q_T` is the single-pass weak-view teacher softmax.
  - The (averaged) `q_T` is used for the soft-CE target, the class marginal and weights, `q_T` in CT-CR, and the seg view of CT-CL.
    It is not used for CTPV, the detection pseudo-labels or the final prediction.
  - It fires on about 97-99% of frames.

### 4. L_CTCR
`_ctcr_loss` (l.793), mode `soft_seg_global`.
- Detection class to semantic class: `(11..18)` for person, rider, car, truck, bus, train, motorcycle, bicycle.
- Every pixel inside a pseudo-box gets the hard target `sigma(c)`.
- Weight: `w = 0.2 + 0.8 * q_T(p, sigma(c))`, with `q_T` detached.
- Outside all boxes: target 255 (`ignore_index`) and weight 0.
- Overlaps: boxes are processed in detector order and the last box overwrites both target and weight.
  The detector order is score-descending, so the lowest-score box usually wins.
- `L_CTCR = sum(w * CE) / (sum(w) + 1e-6)`, one global normalisation over all supervised pixels, not per box.
- Added with weight 0.3.
- Requirements: `weight>0`, not det-only/seg-only, `(det_gate or seg_gate)`, at least one pseudo-box.
  It is **not blocked** by the score-EMA gate.
- The pseudo-boxes it uses are those after dynamic thresholds, and after CTPV if enabled.

### 5. CT-CL (if enabled; off in CTCMT)
`_ctcl_loss` (l.720), `_supcon_loss` (l.99).
- One FPN level only: the last of `roi_heads.box_in_features` (p5).
- `z_det = L2(mean_{7x7} RoIAlign(F_p5, box))`.
- `z_seg = L2( sum_{p in box} q_T(p, sigma(c)) F_p / max(sum q_T, 1e-6) )`. This is an integer crop, not RoIAlign.
- Raw features: **no learned projection heads**. `_proj_det/_proj_seg` stay `None`. `CTCL_PROJ_DIM` is unused.
- SupCon, temperature 0.07, label = detection class.
  All same-class pairs are positives (det-det, seg-seg, det-seg). The mean is taken over anchors that have at least one positive.
- Requires `det_gate and seg_gate`, so the score gate disables it. Ablation weight is 0.5.

### 6. CTPV (if enabled; off in CTCMT)
`_ctpv_filter` (l.1800). Hard filter.
- `r = mean over box pixels of [argmax_k q_T = sigma(c)]`, computed on the **weak single-pass** teacher softmax.
- Keep the box if `r >= 0.3`, otherwise reject. No down-weighting.
- Unmapped classes (or class index out of range) are kept. Empty boxes are rejected.
- The filtered set feeds the det loss, CT-CR and CT-CL. It does not depend on the score gate.

### 7. Gating
`_teacher_pseudo` (l.625).
- `m` = EMA of the mean score of detections with score > 0.1.
- `r = mean_score / m`.
- The gate closes iff `r > 1.4` or `1/r > 1.4`, i.e. a sharp change in **either** direction.
- Update: `m <- 0.7*m + 0.3*mean_score`. It runs also when the gate is closed.
- Closed also when the teacher has no detection, or none with score > 0.1.
  In those early-return paths `m` and the thresholds are not updated.
  If all scores are <= 0.1, the raw detector output is returned without dynamic filtering.
- The gate sets `det_gate`. It switches off **only** `L_det` and CT-CL.
  Seg soft-CE, anchor KL and CT-CR continue; the optimizer step, EMA and restore always run.
- The per-task, directional and skip variants exist but are off.

### 8. EMA
`_update_teacher` (l.1582). Every frame: `teacher = 0.9998*teacher + 0.0002*student` for all float state, and non-float entries are copied.
The teacher gets no gradients.

### 9. Stochastic restore
`_stochastic_restore` (l.1592). Every frame, after EMA.
- For each trainable `weight/bias` of the **student**, a Bernoulli element mask with `p = RST_M = 0.01` replaces entries with the
  frozen source snapshot (copied from the anchor).
- For keys starting with `backbone.`, `fpn.` or `proposal_generator.anchor_generator.`: `p = 0.01 * 0.1 = 0.001`
  (`CROSS_TASK_FISHER=True`, `BACKBONE_RST_FACTOR=0.1`).
- There is **no Fisher computation** in this path. The flag name is historical.
- The teacher is not restored directly; it follows the student through the EMA.

### 10. Evaluation
`tools/train_net.py --eval-only`, then `Trainer.test`. The log confirms `eval_only=True` and "Start inference on 400 batches" for 400 images.
- Test loader batch size 1, one persistent model across all datasets, no reset, one pass per dataset in the order of `DATASETS.TEST`.
- The prediction is returned by the **EMA teacher** on the weak view, after this frame's update.
- Detection and semantic outputs are evaluated separately (no panoptic combine).
- The long-term streams repeat the same dataset list (ACDC x10, CSC 5 corruptions x10).
- GT is never used in adaptation (`CTCMT_MASK_DIAG_GT_ROOT` is logging only).

## 2. Slide-by-slide corrections

Severity: **MAJOR** = equation or text must change; **MINOR** = add a clarification; OK = no change.
Categories A-D as requested: A correct, B mostly correct, C mismatch, D explored/reference only.

| Slide | Sev. | Cat. | Change |
|---|---|---|---|
| 1, 3, 8, 14 | OK | A | None. |
| 2 | MINOR | B | Add "prediction = EMA teacher after each update". Note that LT rounds revisit the same frames. |
| 4 | MINOR | B | EMA Teacher also "produces the evaluated predictions (weak view)". Add EMA 0.9998; SGD lr 1e-3, momentum 0.9, wd 1e-4. |
| 5 | **MAJOR** | B | Add step 9 "predict with teacher, weak view, after the update (adapt-then-predict)". Steps 1/4 say weak/strong. `L_det` applies only when the gate is open and there is at least one pseudo-box. Add `pred = teacher(x_t)` to the listing. |
| 6 | **MAJOR** | C | Threshold clip is `[0.70, 0.90]` on ACDC and `[0.70, 0.80]` on CSC (the slide says 0.80 only). Add the rule "class without detections: unchanged". Replace the gate text: it skips `L_det` and CT-CL when `r>1.4` or `r<1/1.4` (either direction); seg, anchor, CT-CR continue. Add the equations of section 1.2 and 1.7. |
| 7 | **MAJOR** | B | Losses are correct. Add the aug-avg details: anchor confidence < 0.95, scales {0.75, 1, 1.25} x 2 flips, strong view, fires ~97-99%. Add class weights `m_k^-0.5` (EMA 0.999), anchor weight 0.1, strong-view anchor. |
| 9 | **MAJOR** | C/D | Remove `phi_det`, `phi_seg` (no projection heads). `z_seg` is a weighted crop, not RoIAlign. p5 only. Positives are all same-class pairs. Disabled by the gate. Keep "not retained". |
| 10 | MINOR | B | Equations correct. Add: `Omega_CT` = union of boxes; outside = ignore; last box overwrites on overlap; global normalisation; not gated; `q_T` detached and possibly aug-averaged; sigma = trainIds 11..18. |
| 11 | MINOR | B/D | Equations correct. Add `tau_V = 0.3`, hard reject, weak single-pass teacher, unmapped classes kept. |
| 12 | OK | A | Add: CT-CL weight 0.5, CTPV 0.3; Base (16.999) is a different run set from slide 20 (16.957). |
| 13 | **MAJOR** | C | "Full MTL" (24.80/30.83) is `e13a` = **CT-CL 0.5 + CT-CR 0.3** plus the base; it is not Base. Add "CSC-LT". Seed basis is inconsistent: Full MTL, SEG-only and Source are seed 0; DET-only (26.93/35.70) is a 3-seed mean (seed 0: 26.80/35.51). "OFF" means the loss is disabled; the head is not frozen. |
| 15 | **MAJOR** | C | "31.66 -> 35.2 (R4) -> 33.6" is the **Semantic-FPN specialist (ST-S)**, a different source architecture. For the Panoptic MTL seg-only arm the numbers are 27.21 -> 29.2 (R3) -> 26.7 (R10). "Routed SEG" (`aux_head_only`) blocks **all** non-detection losses (seg, anchor, CT-CR, CT-CL) from the whole backbone; these runs also had CT-CL on. |
| 16 | OK | A | Add: λ=1.0 on ACDC4 diverged (NaN); random order uses seed 2026. |
| 17 | **MAJOR** | C/D | There is no Fisher over the source likelihood. Importance is the online squared gradient of the **adaptation loss**. `fisher_guided_restore` restores the **lowest**-importance entries. `fisher_xtask` keeps EMA(0.99) of `g_det^2` and `g_aux^2` on ResNet and, after 50 warm-up updates, scales the lower-importance task by λ=0.5 at element-wise conflicts. Remove "static" and "protect high-F". These variants exist only in `ctcmt_mtl_with_fisher_30647ff.py` (l.1623, l.1830). |
| 18 | **MAJOR** | C/D | `g_seg = grad(L_seg + 0.1 L_anchor)`: the anchor term is in the `seg` loss group, not in `g_reg`. `g_reg` holds CT-CR (and CT-CL/proto if on). The method is the Gradient Consensus of CoCo-MT-TTA (c=0.5, 100 Adam steps, lr 1.0), not the repo's `cagrad` mode. It applies to `backbone.*` only and falls back to the joint gradient when det or seg loss is absent (`_backward_task_coco`, l.1232). |
| 19 | MINOR | B | The final objective is correct. Add to "Retained": dynamic per-class thresholds, score-EMA gate (det only), strong-aug student, conditional aug-averaging, anchor marginals. "Task-aware restoration" = Bernoulli restore p=0.01 (heads) / 0.001 (backbone+FPN), not Fisher. |
| 20-21 | OK | A | Numbers verified. Footnote: Base = same pipeline minus CT-CR. `tau_max` = 0.9 ACDC / 0.8 CSC. |
| 22, 24, 25 | OK | n/a | Not verifiable from code. |
| 23 | MINOR | B | "5.88 GB" is 5880 MiB = 5.74 GiB. Add: 400 frames after 50 warm-up, 3 repeats, `defocus_blur_mtl`. "Plain joint" = `newsrc_csc_ctcr` (conflict none); "headline path" = `lambda=1` resnet_route. |

## 3. Caveat the deck should not overclaim

Seed-0 runs without restore (`RST_M=0`, `paper26_fisher_norestore_*`, `CONFLICT_MODE=none`) are not worse than the headline:

| Config | ACDC4 AP50 / mIoU | CSC12 AP50 / mIoU |
|---|---|---|
| Headline (restore on) | 38.29 / 37.79 | 18.03 / 30.24 |
| No restore | 39.40 / 38.09 | 18.09 / 30.10 |

There is no no-restore long-term run, so the deck must not claim that restoration improves short-term results.
Keep "task-aware restoration" as a design component, not as a measured gain.

## 4. Not verified

- Figures (`method.png`, `semantic_segm.png`, `ctcr.png`, ...). Check that `semantic_segm.png` does not show the weak view for the aug-avg target.
- Slide 22 and 24 numbers (CTAOD per round, DAT-BF).
- Byte-identity of the code behind the `e13a..e22` runs (see the stability check above).
