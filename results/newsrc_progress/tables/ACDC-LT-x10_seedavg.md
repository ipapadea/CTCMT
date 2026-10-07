# ACDC-LT-x10 — averaged over seeds

| arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | fisher_rst | v2_backbone | n | AP50 | mIoU | R10_AP50 | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | true | 2 | 43.760 ± 0.489 | 39.069 ± 1.619 | 43.841 ± 0.014 | 38.981 ± 1.604 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 12 | 43.273 ± 1.818 | 38.089 ± 1.615 | 44.736 ± 2.007 | 38.119 ± 1.512 |
| AMROD | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | 1 | 39.002 |  | 40.204 |  |
| TENT_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | 1 |  | 32.017 |  | 31.591 |
| CoTTA_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | 1 |  | 20.174 |  | 13.984 |
