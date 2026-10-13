# CTCMT paper — experiment handoff (2026-10-08)

## Canonical rules
- Repository: ipapadea/CTCMT, branch `extension-implementation`. Local repo `/media/ilias/DATA/ilias/AMROD`.
- Canonical source: `/workspace/output/panoptic_fpn_R50_cityscapes_segw1/model_final.pth`. Do not mix with old source.
- Headline: mean-teacher multitask CTTA + detection pseudo-labels + semantic soft consistency + source anchor (0.1) + CT-CR (`soft_seg_global`, weight 0.3, floor 0.2). CTCL and CTPV disabled. Full auxiliary gradient access λ=1.
- Main headline Base/Task-CoCo/Ours n=3; detailed ablation/routing n=1 unless rerun. IMPORTANT: committed Task-CoCo configs inherit CT-CR, so benchmarked Task-CoCo includes CT-CR plus Task-CoCo routing; verify provenance before reporting.
- A8 frozen retention complete; A9a gradient (CSC12, 401 valid samples), A9b spatial support (168339 pseudo-boxes), A9c paired object recall and A9d mechanism correlations complete. A10 legacy old-source diagnostic: keep separate.
- Current cleaned TeX artifact: `experimental_results_clean.tex` in conversation; do not silently overwrite original.

## Eight agreed next tasks — priority and execution
1. **Efficiency** (MUST): Base / Task-CoCo / Ours same GPU, same CSC12 representative inputs; wall-time ms/image, throughput, peak GPU memory, trainable params; warmup and synchronize CUDA. Include adaptation and inference costs distinctly. First implement measurement instrumentation, then batch runs.
2. **CT-CR loss-weight sensitivity** (MUST): λ_CTCR = {0, 0.1, 0.3, 0.5, 1.0}, seed0 on CSC12 and ACDC4 if budget allows. All else fixed; λ_CTCR=0 should be checked against Base behavior. Use unique configs and outputs; do not edit canonical configs.
3. **Qualitative joint figure**: select fixed examples from car/person improvements, truncated boxes, bus/motorcycle failures, snow gate; render Input/Source/Base/Ours/GT and optional CT-CR support. Requires matched model states and inference exports, not necessarily new full training.
4. **Multi-seed component ablation**: CTCR, CTCL, CTCR+CTCL, CTCR+CTCL+CTPV vs Base; prioritize CSC12 seeds 0/1/2, reuse existing matching runs only after checking protocol. Existing LT seed0 table is not multi-seed. Do not claim full LT multi-seed from CSC12.
5. **Stream-order robustness**: canonical, reverse, seeded random order, identical corruptions and counts; Base vs Ours; preferably ≥3 seeds or clearly mark exploratory seed0. Ensure stream runner actually honors override and uses uninterrupted adaptation.
6. **Detection metrics**: extract AP/AP50/AP75 (possibly APs/APm/APl) from existing evaluation logs first; avoid GPU reruns unless missing.
7. **Generalization** (optional high cost): additional target dataset or backbone with compatible detection/semantic mapping; plan only after core runs.
8. **2025–26 baselines** (high cost): shortlist method with released code and compatible backbone/tasks/protocol; reproduce under identical source/evaluation. Do not mix published unmatched numbers in main table.

## GPU batch plan (prepare before launch)
- Phase 0: inspect scripts/config inheritance, checkpoint existence, datasets, GPU model/VRAM, disk, existing outputs, log retention. Capture `git rev-parse HEAD`, `git status`, `nvidia-smi` and config dumps.
- Phase 1 concurrent: GPU A = CT-CR weight sweep; GPU B = multi-seed component ablation; GPU C (if available) = order robustness. Never run two GPU-heavy experiments on the same device without explicit scheduling.
- Phase 2: efficiency sequentially on an otherwise idle *same GPU*; qualitative inference on spare GPU; AP extraction CPU only.
- Phase 3: optional extra backbone and recent baseline reproduction after audit.
- Unique experiment names: `paper26_weight_csc12_w{0p0,0p1,0p3,0p5,1p0}_s0`; `paper26_ablate_csc12_{base,ctcr,ctcl,both,all}_s{0,1,2}`; `paper26_order_csc12_{canonical,reverse,random}_s0`.
- Per run save config YAML, git SHA, seed, stream, source checkpoint hash, stdout log, metrics JSON/CSV, wall time, GPU name, exit code. Preserve original outputs.
- Launch only after verifying actual CLI/config keys and stream semantics against the repository. Avoid inventing commands or changing a live canonical run.

## Existing headline (n=3)
Short ACDC4 Base 36.839±.072 AP50 /36.864±.172 mIoU; Task-CoCo 37.749±.315 /37.556±.230; Ours 38.007±.254 /37.800±.064.
Short CSC12 Base 16.957±.291 /28.948±.665; Task-CoCo 17.267±.328 /29.921±.203; Ours 17.722±.264 /30.073±.189.
LT ACDC Base 42.494±.090 /41.219±.087; Task-CoCo 43.369±.129 /41.632±.230; Ours 44.076±.357 /41.921±.256.
LT CSC Base 25.266±.511 /33.677±.251; Task-CoCo 25.806±.299 /32.733±.216; Ours 26.725±.463 /33.334±.320.

## A9 final
A9a CSC12 401 valid samples: detection mean norm 6.667, seg 4.567 (0.69×), CTCR 4.093 (0.61×); det-vs-CTCR mean cosine .1628/conflict 18.2%; det-vs-seg .0468/32.4%; FPN cosine .0282/conflict 19.2%; res3 .2081/16.5%, res4 .1926/12.2%, res5 .1411/10.7%. Snow zero CTCR gradient samples.
A9b 168339 boxes: rectangle precision/recall/IoU .6799/1/.6799; semantic τ=.7 .8398/.9317/.7911, τ=.9 .9005/.8684/.7924; detector mask τ=.5 .8579/.8396/.7371. Hard support masks are counterfactual diagnostics, not headline soft_seg_global objective.
A9c matched object recall Δ +.06787 vs control rerun noise −.00228; strongest car +.10052, person +.06062; bus −.00639 and motorcycle −.00292.
A9d Spearman Δrecall: box coverage −.33052, correct target fraction +.47079, wrong target fraction −.05711, correct object weight +.37636, wrong object weight −.11575. Correlations descriptive, not causal.

## Next action
Audit actual repository scripts and config overrides; generate a manifest and dry-run batch launcher before starting GPU runs. Start with weight sensitivity + multi-seed ablation. Keep an experiment ledger with statuses and outcomes, and update this handoff after each batch.
