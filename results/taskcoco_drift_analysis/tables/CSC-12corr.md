# CSC-12corr

(13 runs)

| run | arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | v2_backbone | seed | n_evals | AP50 | mIoU | R1_AP50 | R10_AP50 | R1_mIoU | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| tent_newsrc_csc12_s0 | TENT_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 12 |  | 27.257 |  |  |  |  |
| cotta_newsrc_csc12_s0 | CoTTA_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 12 |  | 26.015 |  |  |  |  |
| tent_pfnsrc_csc12_s0 | TENT_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 12 |  | 25.768 |  |  |  |  |
| cotta_pfnsrc_csc12_s0 | CoTTA_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 12 |  | 24.140 |  |  |  |  |
| e11_bothsc_ctcrD_csc12_s42 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 42 | 12 | 17.599 | 28.969 |  |  |  |  |
| e11_bothsc_ctcrD_csc12_s123 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 123 | 12 | 17.479 | 28.838 |  |  |  |  |
| e25_detonly_csc12_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 12 | 17.398 | 29.295 |  |  |  |  |
| e24_seghead_only_csc12_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 12 | 17.371 | 29.012 |  |  |  |  |
| e11_bothsc_ctcrD_csc12_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 12 | 17.011 | 28.708 |  |  |  |  |
| e27_s6_entropy_csc12_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 12 | 16.988 | 28.713 |  |  |  |  |
| amrod_newsrc_csc12_s0 | AMROD | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 12 | 15.788 |  |  |  |  |  |
| amrod_pfnsrc_csc12_s0 | AMROD | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 12 | 15.076 |  |  |  |  |  |
| source_only_pfn_cs_c | PanopticFPN | panoptic_fpn_R50_cityscapes | 0.005 | 0.99 | false | full_box | 0.0 | 0.01 |  |  |  | false | -1 | 12 | 12.697 | 26.253 |  |  |  |  |
