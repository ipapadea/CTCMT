# ACDC-1evals

(8 runs)

| run | arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | v2_backbone | seed | n_evals | AP50 | mIoU | R1_AP50 | R10_AP50 | R1_mIoU | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| smoke_newsrc_taskcoco_acdc | CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.0 | true | true | 0.1 | true | 0 | 1 | 55.399 | 44.434 |  |  |  |  |
| smoke_newsrc_ctcr_rblock_acdc | CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.0 | true | true | 0.1 | true | 0 | 1 | 54.721 | 44.006 |  |  |  |  |
| smoke_newsrc_ctcr_r25_acdc | CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.0 | true | true | 0.1 | true | 0 | 1 | 54.693 | 43.998 |  |  |  |  |
| smoke_ctcmt_e11_bothsc_ctcrD | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 1 | 53.913 | 40.492 |  |  |  |  |
| eval_acdc_new_w10 | PanopticFPN |  | 0.005 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | -1 | 1 | 53.601 | 42.748 |  |  |  |  |
| smoke_e24_acdc | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | 0 | 1 | 52.179 | 39.209 |  |  |  |  |
| smoke_cotta_newsrc_acdc_s0_20260925_004725_1794148 | CoTTA_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 1 |  | 43.261 |  |  |  |  |
| smoke_tent_newsrc_acdc_s0_20260925_004725_1794148 | TENT_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | 0 | 1 |  | 43.259 |  |  |  |  |
