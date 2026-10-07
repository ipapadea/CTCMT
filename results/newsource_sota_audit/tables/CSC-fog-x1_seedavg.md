# CSC-fog-x1 — averaged over seeds

| arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | v2_backbone | n | AP50 | mIoU | R10_AP50 | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TENT_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 1 |  | 40.504 |  |  |
| CoTTA_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 2 |  | 39.940 ± 0.000 |  |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.0 | true | true | 0.1 | true | 2 | 39.478 ± 0.000 | 42.444 ± 0.000 |  |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 7 | 37.637 ± 1.857 | 39.907 ± 1.093 |  |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.0 | 0.5 | true | true | 0.1 | true | 1 | 36.943 | 39.399 |  |  |
