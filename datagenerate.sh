#!/bin/bash

# Default mode value
mode="test"
save_dir=""

# Check if arguments are provided
if [ $# -eq 1 ]; then
    if [ "${1#--save-dir=}" != "$1" ]; then
        save_dir="${1#*=}"
    else
        mode=$1
    fi
elif [ $# -eq 2 ]; then
    mode=$1
    if [ "${2#--save-dir=}" != "$2" ]; then
        save_dir="${2#*=}"
    fi
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

# Function to run test command
run_test() {
    local config=$1
    local checkpoint=$2
    
    cmd="python tools/test.py $config $checkpoint --eval mAP"
    if [ -n "$save_dir" ]; then
        cmd="$cmd --save-dir $save_dir"
    fi
    
    echo "Running command: $cmd"
    $cmd
}

# Run the first command
config1=$(get_config_file "configs/tr3d/tr3d_sunrgbd-3d-10class.py")
run_test "$config1" "checkpoints/tr3d_sunrgbd.pth"

# Run the second command
config2=$(get_config_file "configs/tr3d/tr3d_s3dis-3d-5class.py")
run_test "$config2" "checkpoints/tr3d_s3dis.pth"

# Run the third command
config3=$(get_config_file "configs/tr3d/tr3d_scannet-3d-18class.py")
run_test "$config3" "checkpoints/tr3d_scannet.pth"