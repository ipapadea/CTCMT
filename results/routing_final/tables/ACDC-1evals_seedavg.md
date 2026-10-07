# ACDC-1evals — averaged over seeds

| arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | v2_backbone | n | AP50 | mIoU | R10_AP50 | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.0 | true | true | 0.1 | true | 3 | 54.938 ± 0.400 | 44.146 ± 0.249 |  |  |
| PanopticFPN |  | 0.005 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 1 | 53.601 | 42.748 |  |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 2 | 53.046 ± 1.226 | 39.850 ± 0.907 |  |  |
| CoTTA_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 1 |  | 43.261 |  |  |
| TENT_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 1 |  | 43.259 |  |  |
