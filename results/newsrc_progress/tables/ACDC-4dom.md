# ACDC-4dom

(18 runs)

| run | arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | fisher_rst | v2_backbone | seed | n_evals | AP50 | mIoU | R1_AP50 | R10_AP50 | R1_mIoU | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| e10_both_acdc_seed0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | full_box | 0.3 | 0.5 | true |  | 0.1 | false | true | 0 | 4 | 38.748 | 34.635 |  |  |  |  |
| e11_bothsc_ctcrD_acdc4_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 4 | 38.379 | 35.771 |  |  |  |  |
| e11_bothsc_ctcrD_acdc4_s42 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 42 | 4 | 38.344 | 35.967 |  |  |  |  |
| e9_strongaug_seed0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | full_box | 0.3 | 0.5 |  |  |  | false | true | 0 | 4 | 38.194 | 35.428 |  |  |  |  |
| e11_bothsc_ctcrD_acdc4_s123 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 123 | 4 | 37.887 | 35.865 |  |  |  |  |
| e9_fisher_seed0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | false | full_box | 0.3 | 0.5 |  |  |  | true | true | 0 | 4 | 37.780 | 35.466 |  |  |  |  |
| ctcr_D_acdc_seed123 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 |  | soft_seg_global | 0.3 | 0.5 |  |  |  |  | true | 123 | 4 | 37.157 | 35.062 |  |  |  |  |
| ctcr_D_acdc_seed42 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 |  | soft_seg_global | 0.3 | 0.5 |  |  |  |  | true | 42 | 4 | 37.129 | 34.938 |  |  |  |  |
| ctcr_D_acdc_seed0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 |  | soft_seg_global | 0.3 | 0.5 |  |  |  |  | true | 0 | 4 | 36.937 | 35.051 |  |  |  |  |
| e27_s6_entropy_acdc4_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 4 | 36.936 | 33.885 |  |  |  |  |
| e25_detonly_acdc4_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 4 | 36.913 | 33.889 |  |  |  |  |
| e24_seghead_only_acdc4_s0 | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | 0 | 4 | 36.833 | 34.029 |  |  |  |  |
| amrod_pfnsrc_seed0 | AMROD | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 |  |  |  | false | false | 0 | 4 | 35.900 |  |  |  |  |  |
| eval_acdc_new_48k_w10 | PanopticFPN |  | 0.005 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | -1 | 4 | 34.260 | 35.000 |  |  |  |  |
| eval_acdc_old_w05 | PanopticFPN | panoptic_fpn_R50_cityscapes | 0.005 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | -1 | 4 | 34.208 | 32.202 |  |  |  |  |
| source_only_pfn_acdc_full | PanopticFPN | panoptic_fpn_R50_cityscapes | 0.005 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | 0 | 4 | 34.208 | 32.202 |  |  |  |  |
| tent_pfnsrc_seed0 | TENT_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 |  |  |  | false | false | 0 | 4 |  | 32.227 |  |  |  |  |
| cotta_pfnsrc_seed0 | CoTTA_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 |  |  |  | false | false | 0 | 4 |  | 30.883 |  |  |  |  |
