# CSC-fog-x1

(8 runs)

| run | arch | source | w_ctcr | seed | n_evals | AP50 | mIoU | R1_AP50 | R10_AP50 | R1_mIoU | R10_mIoU |
|---|---|---|---|---|---|---|---|---|---|---|---|
| smoke_e17_cagrad | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.3 | 0 | 1 | 39.343 | 41.162 |  |  |  |  |
| smoke_e16_protectedgrad | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.3 | 0 | 1 | 38.777 | 40.378 |  |  |  |  |
| smoke_e18_harddecouple | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.3 | 0 | 1 | 38.734 | 40.382 |  |  |  |  |
| diag_ctcr_priors | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.3 | 0 | 1 | 38.631 | 40.337 |  |  |  |  |
| smoke_e20_dynweight | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.3 | 0 | 1 | 37.226 | 39.782 |  |  |  |  |
| smoke_e23_detseg_nocross | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.0 | 0 | 1 | 36.943 | 39.399 |  |  |  |  |
| smoke_e22_seghead_only | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.3 | 0 | 1 | 36.762 | 39.600 |  |  |  |  |
| smoke_e19_frozentrunk | CTCMT_MTL | panoptic_fpn_R50_cityscapes | 0.3 | 0 | 1 | 33.984 | 37.706 |  |  |  |  |
