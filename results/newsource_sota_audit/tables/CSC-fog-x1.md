# CSC-fog-x1

(13 runs)

| run | arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | v2_backbone | seed | n_evals | AP50 | mIoU | R1_AP50 | R10_AP50 | R1_mIoU | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| smoke_tent_newsrc_csc_s0_20260925_004725_1794148 | TENT_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 1 |  | 40.504 |  |  |  |  |
| smoke_cotta_newsrc_csc_s0_20260925_004725_1794148 | CoTTA_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 1 |  | 39.940 |  |  |  |  |
| smoke_cotta_newsrc_csc_retry_s0 | CoTTA_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 1 |  | 39.940 |  |  |  |  |
| launch_partial_csc | CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.0 | true | true | 0.1 | true | 0 | 1 | 39.478 | 42.444 |  |  |  |  |
| newsrc_ctcr_r25_cscLT_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.0 | true | true | 0.1 | true | 0 | 1 | 39.478 | 42.444 |  |  |  |  |
| smoke_e17_cagrad | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 1 | 39.343 | 41.162 |  |  |  |  |
| smoke_e16_protectedgrad | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 1 | 38.777 | 40.378 |  |  |  |  |
| smoke_e18_harddecouple | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 1 | 38.734 | 40.382 |  |  |  |  |
| diag_ctcr_priors | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 1 | 38.631 | 40.337 |  |  |  |  |
| smoke_e20_dynweight | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 1 | 37.226 | 39.782 |  |  |  |  |
| smoke_e23_detseg_nocross | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.0 | 0.5 | true | true | 0.1 | true | 0 | 1 | 36.943 | 39.399 |  |  |  |  |
| smoke_e22_seghead_only | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 1 | 36.762 | 39.600 |  |  |  |  |
| smoke_e19_frozentrunk | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 1 | 33.984 | 37.706 |  |  |  |  |
