# CSC-LT-x10 — averaged over seeds

| arch | source | lr | mt | strong_aug | ctcr_mode | w_ctcr | w_ctcl | cls_bal | scale_pres | anchor_marg | fisher_rst | v2_backbone | ctpv | n | AP50 | mIoU | R10_AP50 | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CTCMT_MTL | semantic_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | false | 1 |  | 34.393 |  | 33.587 |
| TENT_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 1 |  | 27.781 |  | 26.524 |
| CTCMT_MTL | mask_rcnn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | false | 1 | 27.237 |  | 29.159 |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.0 | true | true | 0.1 | false | true | false | 6 | 27.218 ± 0.560 | 33.857 ± 0.464 | 30.133 ± 0.777 | 32.791 ± 0.947 |
| CoTTA_SemSeg | panoptic_fpn_R50_cityscapes_segw1 | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 1 |  | 26.731 |  | 26.464 |
| AMROD | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 1 | 26.403 |  | 31.099 |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | true | true | false | 2 | 26.394 ± 1.544 | 33.669 ± 1.955 | 27.262 ± 2.573 | 33.098 ± 2.375 |
| AMROD | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 2 | 26.149 ± 0.000 |  | 30.684 ± 0.000 |  |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.0 | 0.5 | true | true | 0.1 | false | true | false | 2 | 25.594 ± 0.542 | 32.652 ± 0.987 | 29.032 ± 0.768 | 33.423 ± 2.846 |
| TENT_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 1 |  | 25.530 |  | 23.949 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.0 | 0.0 | true | true | 0.1 | false | true | false | 1 | 25.352 | 33.667 | 28.820 | 33.332 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.0 | 0.5 | true | true | 0.1 | false | true | false | 1 | 24.855 | 33.634 | 26.810 | 32.750 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | false | 29 | 24.457 ± 2.774 | 31.843 ± 2.347 | 25.517 ± 3.872 | 30.246 ± 3.879 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | false | 1 | 24.007 | 32.173 | 24.211 | 29.876 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | full_box | 0.3 | 0.5 | true | true | 0.1 | true | true | false | 1 | 23.996 | 32.744 | 23.642 | 31.811 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | full_box | 0.3 | 0.5 | false | false | 0.0 | false | true | false | 1 | 23.830 | 28.714 | 24.335 | 25.121 |
| CoTTA_SemSeg | panoptic_fpn_R50_cityscapes | 0.0001 | 0.99 | false | full_box | 0.0 | 0.01 | false | false | 0.0 | false | false | false | 1 |  | 23.767 |  | 23.175 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.001 | 0.9998 | true | full_box | 0.3 | 0.5 | true | true | 0.1 | false | true | false | 2 | 23.654 ± 0.481 | 30.995 ± 0.006 | 24.389 ± 0.630 | 28.193 ± 0.007 |
| CTCMT_MTL | panoptic_fpn_R50_cityscapes_segw1 | 0.001 | 0.9998 | true | soft_seg_global | 0.3 | 0.5 | true | true | 0.1 | false | true | true | 1 | 23.426 | 32.024 | 23.220 | 29.625 |
