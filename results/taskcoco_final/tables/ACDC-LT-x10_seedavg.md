# ACDC-LT-x10 — averaged over seeds

| arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | fisher_rst | v2_backbone | ctpv | n | AP50 | mIoU | R10_AP50 | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | false | 1 | 43.818 | 41.896 | 44.858 | 42.059 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | true | false | 2 | 43.760 ± 0.489 | 39.069 ± 1.619 | 43.841 ± 0.014 | 38.981 ± 1.604 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.0 | true | true | 0.1 | false | true | false | 6 | 43.351 ± 0.262 | 40.700 ± 0.626 | 45.341 ± 0.103 | 41.471 ± 0.764 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | false | 12 | 43.273 ± 1.818 | 38.089 ± 1.615 | 44.736 ± 2.007 | 38.119 ± 1.512 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | true | 1 | 43.186 | 41.583 | 42.786 | 41.415 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.0 | 0.5 | true | true | 0.1 | false | true | false | 1 | 42.920 | 41.949 | 44.548 | 43.552 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.0 | 0.0 | true | true | 0.1 | false | true | false | 2 | 42.817 ± 0.597 | 41.502 ± 0.292 | 43.715 ± 1.314 | 42.358 ± 1.333 |
| AMROD | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 1 | 39.002 |  | 40.204 |  |
| AMROD | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 2 | 38.744 ± 0.000 |  | 40.387 ± 0.000 |  |
| TENT_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 1 |  | 35.469 |  | 35.399 |
| TENT_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 1 |  | 32.017 |  | 31.591 |
| CoTTA_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 1 |  | 20.600 |  | 9.555 |
| CoTTA_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 1 |  | 20.174 |  | 13.984 |
