###
The modification to the original repository is the modification of the indoor_eval file, which is used to save the results of the OD of each object for each scene under tr3d/data/sunrgbd/ODResults using the pickle file.


### Prerequisites
In this section we demonstrate how to prepare an environment with PyTorch.
MMDection3D works on Linux, Windows (experimental support) and macOS and requires the following packages:

- Python 3.6+
- PyTorch 1.3+
- CUDA 9.2+ (If you build PyTorch from source, CUDA 9.0 is also compatible)
- GCC 5+
- [MMCV](https://mmcv.readthedocs.io/en/latest/#installation)

```{note}
If you are experienced with PyTorch and have already installed it, just skip this part and jump to the [next section](#installation). Otherwise, you can follow these steps for the preparation.
```

**Step 0.** Download and install Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html).

**Step 1.** Create a conda environment and activate it.

```shell
conda create --name tr3d python=3.8 -y
conda activate tr3d
```

**Step 2.** Install PyTorch following [official instructions](https://pytorch.org/get-started/locally/), e.g.

On GPU platforms:

```shell
conda install pytorch torchvision -c pytorch
```

On CPU platforms:

```shell
conda install pytorch torchvision cpuonly -c pytorch
```


### Installation
This implementation is based on [mmdetection3d](https://github.com/open-mmlab/mmdetection3d) framework.
Please refer to the original installation guide [getting_started.md](docs/en/getting_started.md), including MinkowskiEngine installation, replacing `open-mmlab/mmdetection3d` with `weishuaiSong/tr3dodresult`. 

```shell
pip install openmim
mim install mmcv-full
mim install mmdet
mim install mmsegmentation
git clone https://github.com/weishuaiSong/tr3dodresult
cd tr3dodresult
pip install -e .
```

**Installation of Minkowski Engine**
Remember that you need to install pytorch before you install Minkowski Engine to avoid error

```shell
pip install ninja
conda install openblas-devel -c anaconda
git clone https://github.com/NVIDIA/MinkowskiEngine
cd MinkowskiEngine
python setup.py install --blas_include_dirs=${CONDA_PREFIX}/include --blas=openblas
```

### Data preparation and checkpoint download
We follow the mmdetection3d data preparation protocol described in [scannet](data/scannet), [sunrgbd](data/sunrgbd), and [s3dis](data/s3dis).  
Here we only need to use the sunrgb data  

Download the checkpoints and place them in the tr3dresult\checkpoints directory.  
[model](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_s3dis.pth)



### Data generation

Test pre-trained model using [test](tools/dist_test.sh) with TR3D [configs](configs/tr3d):
```shell
python tools/test.py configs/tr3d/tr3d_sunrgbd-3d-10class.py checkpoints/tr3d_sunrgbd.pth --eval mAP
```
The obtained file will be stored separately under tr3d/data/sunrgbd/ODResults, with the same name as the corresponding point cloud, and the content of the storage is a dictionary, the corresponding key is the object id, and the value is whether or not the object has been detected, and if it is then 1 otherwise 0.


**TR3D 3D Detection**

| Dataset | mAP@0.25 | mAP@0.5 | Scenes <br> per sec.| Download |
|:-------:|:--------:|:-------:|:-------------------:|:--------:|
| ScanNet | 72.9 (72.0) | 59.3 (57.4) | 23.7 | [model](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_scannet.pth) &#124; [log](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_scannet.log.json) &#124; [config](configs/tr3d/tr3d_scannet-3d-18class.py) |
| SUN RGB-D | 67.1 (66.3) | 50.4 (49.6) | 27.5 | [model](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_sunrgbd.pth) &#124; [log](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_sunrgbd.log.json) &#124; [config](configs/tr3d/tr3d_sunrgbd-3d-10class.py) |
| S3DIS | 74.5 (72.1) | 51.7 (47.6) | 21.0 | [model](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_s3dis.pth) &#124; [log](https://github.com/samsunglabs/tr3d/releases/download/v1.0/tr3d_s3dis.log.json) &#124; [config](configs/tr3d/tr3d_s3dis-3d-5class.py) |
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
