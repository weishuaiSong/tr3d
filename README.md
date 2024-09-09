###
This branch was created to extract the results of the tr3d method for object detection on the sunrgb dataset

### Installation
Please refer to the original installation guide [getting_started.md](docs/en/getting_started.md), including MinkowskiEngine installation, replacing `open-mmlab/mmdetection3d` with `samsunglabs/tr3d`.

### Getting Started
Please see [getting_started.md](docs/getting_started.md) for basic usage examples.
We follow the mmdetection3d data preparation protocol described in [scannet](data/scannet), [sunrgbd](data/sunrgbd), and [s3dis](data/s3dis).

**Testing**
This step to extract sunrgb's object detection results on the test set.

Test pre-trained model using [test](tools/dist_test.sh) with TR3D [configs](configs/tr3d):
```shell
python tools/test.py configs/tr3d/tr3d_sunrgbd-3d-10class.py yourcheckpoints/tr3d_sunrgbd.pth --eval mAP
```


```

### Models

The metrics are obtained in 5 training runs followed by 5 test runs. We report both the best and the average values (the latter are given in round brackets).
Inference speed (scenes per second) is measured on a single NVidia RTX 4090. Please, note that ScanNet-pretrained S3DIS model was actually trained in the original
[openmmlab/mmdetection3d](https://github.com/open-mmlab/mmdetection3d/tree/main/projects/TR3D) codebase.

**TR3D 3D Detection**

| Dataset | mAP@0.25 | mAP@0.5 | Scenes <br> per sec.| Download |
|:-------:|:--------:|:-------:|:-------------------:|:--------:|
| SUN RGB-D | 67.1 (66.3) | 50.4 (49.6) | 27.5 | [model](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_sunrgbd.pth) &#124; [log](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_sunrgbd.log.json) &#124; [config](configs/tr3d/tr3d_sunrgbd-3d-10class.py) |
| S3DIS <br> ScanNet-pretrained | 75.9 (75.1) | 56.6 (54.8) | 21.0 | [model](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_scannet-pretrain_s3dis.pth) &#124; [log](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_scannet-pretrain_s3dis.log) &#124; [config](configs/tr3d/tr3d_scannet-pretrain_s3dis-3d-5class.py) |



### Citation

If you find this work useful for your research, please cite our paper:

```
@misc{rukhovich2023tr3d,
  doi = {10.48550/ARXIV.2302.02858},
  url = {https://arxiv.org/abs/2302.02858},
  author = {Rukhovich, Danila and Vorontsova, Anna and Konushin, Anton},
  title = {TR3D: Towards Real-Time Indoor 3D Object Detection},
  publisher = {arXiv},
  year = {2023}
}
```
