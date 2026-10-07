# CSC-12corr — averaged over seeds

| arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | v2_backbone | n | AP50 | mIoU | R10_AP50 | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TENT_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 1 |  | 27.257 |  |  |
| CoTTA_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 1 |  | 26.015 |  |  |
| TENT_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 1 |  | 25.768 |  |  |
| CoTTA_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 1 |  | 24.140 |  |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 6 | 17.308 ± 0.252 | 28.922 ± 0.222 |  |  |
| AMROD | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 1 | 15.788 |  |  |  |
| AMROD | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 1 | 15.076 |  |  |  |
| PanopticFPN | panoptic_fpn_R50_cityscapes | 0.005 | 0.99 | false | full_box | 0.0 | 0.01 |  |  |  | false | 1 | 12.697 | 26.253 |  |  |
