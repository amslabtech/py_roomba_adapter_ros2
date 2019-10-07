#!/bin/bash

tag="latest"

if [ $# -ne 1 ]; then
    echo "docker container tag is not specified"
    echo "default tag 'latest' will be used"
else
    tag=$1
fi

IMAGE_NAME="amslabtech/py_roomba_adapter_ros2:${tag}"
echo $IMAGE_NAME

docker build -t $IMAGE_NAME ./docker
