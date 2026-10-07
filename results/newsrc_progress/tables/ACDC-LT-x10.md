# ACDC-LT-x10

(17 runs)

| run | arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | fisher_rst | v2_backbone | seed | n_evals | AP50 | mIoU | R1_AP50 | R10_AP50 | R1_mIoU | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| e27_s6_entropy_acdc_acdcLT_s42 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 42 | 40 | 44.354 | 36.337 | 38.001 | 46.289 | 33.671 | 36.267 |
| e27_s6_entropy_acdc_acdcLT_s123 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 123 | 40 | 44.215 | 36.737 | 37.278 | 45.858 | 33.261 | 37.120 |
| e32_fisher_full_acdcLT_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | true | 0 | 40 | 44.106 | 40.213 | 39.095 | 43.831 | 36.351 | 40.115 |
| e11_bothsc_ctcrD_acdcLT_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 40 | 43.984 | 39.800 | 38.394 | 44.844 | 35.707 | 39.469 |
| e27_s6_entropy_acdc_acdcLT_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 40 | 43.970 | 36.458 | 37.138 | 45.651 | 32.998 | 35.755 |
| e38_fpn_routing_acdcLT_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 40 | 43.887 | 39.901 | 38.550 | 44.599 | 35.734 | 39.623 |
| e11_bothsc_ctcrD_acdcLT_s42 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 42 | 40 | 43.884 | 40.326 | 38.263 | 44.584 | 36.199 | 39.717 |
| e11_bothsc_ctcrD_acdcLT_s123 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 123 | 40 | 43.557 | 39.954 | 37.900 | 44.793 | 35.833 | 39.810 |
| e24_seghead_only_acdc_acdcLT_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 40 | 43.464 | 37.641 | 37.054 | 45.443 | 33.918 | 37.306 |
| batch_acdc_s6 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 80 | 43.424 | 38.246 | 40.171 | 45.443 | 34.900 | 37.306 |
| e33_fisher_s6_acdcLT_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | true | 0 | 40 | 43.415 | 37.924 | 37.798 | 43.851 | 34.448 | 37.847 |
| e25_detonly_acdc_acdcLT_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 40 | 43.384 | 38.850 | 37.077 | 45.672 | 33.959 | 40.016 |
| amrod_pfnsrc_acdcLT_s0 | AMROD | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | 0 | 40 | 39.002 |  | 35.950 | 40.204 |  |  |
| e29_segonly_acdc_acdcLT_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 40 | 37.880 | 36.381 | 35.145 | 38.921 | 33.637 | 37.485 |
| e29_segonly_acdc_acdcLT_s0.segonly-noDet | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 40 |  | 36.438 |  |  | 33.678 | 37.553 |
| tent_pfnsrc_acdcLT_s0 | TENT_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | 0 | 40 |  | 32.017 |  |  | 32.227 | 31.591 |
| cotta_pfnsrc_acdcLT_s0 | CoTTA_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | 0 | 40 |  | 20.174 |  |  | 30.883 | 13.984 |
