# ACDC-4dom — averaged over seeds

| arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | fisher_rst | v2_backbone | n | AP50 | mIoU | R10_AP50 | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | full_box | 0.3 | 0.5 | true |  | 0.1 | false | true | 1 | 38.748 | 34.635 |  |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | full_box | 0.3 | 0.5 |  |  |  | false | true | 1 | 38.194 | 35.428 |  |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | false | full_box | 0.3 | 0.5 |  |  |  | true | true | 1 | 37.780 | 35.466 |  |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 6 | 37.549 ± 0.739 | 34.901 ± 1.062 |  |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 |  | soft_seg_global | 0.3 | 0.5 |  |  |  |  | true | 3 | 37.074 ± 0.120 | 35.017 ± 0.068 |  |  |
| AMROD | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 |  |  |  | false | false | 1 | 35.900 |  |  |  |
| PanopticFPN |  | 0.005 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | 1 | 34.260 | 35.000 |  |  |
| PanopticFPN | panoptic_fpn_R50_cityscapes | 0.005 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | 2 | 34.208 ± 0.000 | 32.202 ± 0.000 |  |  |
| TENT_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 |  |  |  | false | false | 1 |  | 32.227 |  |  |
| CoTTA_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 |  |  |  | false | false | 1 |  | 30.883 |  |  |
