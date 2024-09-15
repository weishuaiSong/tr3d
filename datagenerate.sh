#!/bin/bash

# Default value for mode
mode="test"

# Check if an argument is provided
if [ $# -eq 1 ]; then
    mode=$1
fi

# Function to get the correct config file name
get_config_file() {
    local config=$1
    if [ "$mode" = "all" ]; then
        echo "${config%.*}all.py"
    else
        echo "$config"
    fi
}

# Run the first command
config1=$(get_config_file "configs/tr3d/tr3d_sunrgbd-3d-10class.py")
echo "Running: python tools/test.py $config1 checkpoints/tr3d_sunrgbd.pth --eval mAP"
python tools/test.py $config1 checkpoints/tr3d_sunrgbd.pth --eval mAP


# Run the second command
config2=$(get_config_file "configs/tr3d/tr3d_s3dis-3d-5class.py")
echo "Running: python tools/test.py $config2 checkpoints/tr3d_s3dis.pth --eval mAP"
python tools/test.py $config2 checkpoints/tr3d_s3dis.pth --eval mAP

# # Run the third command
config3=$(get_config_file "configs/tr3d/tr3d_scannet-3d-18class.py")
echo "Running: python tools/test.py $config3 checkpoints/tr3d_scannet.pth --eval mAP"
python tools/test.py $config3 checkpoints/tr3d_scannet.pth --eval mAP