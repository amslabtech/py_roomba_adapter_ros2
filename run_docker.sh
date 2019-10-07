#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

IMAGE_NAME="amslabtech/py_roomba_adapter_ros2"

echo $IMAGE_NAME

docker run -it --rm \
  --net="host" \
  --volume="$SCRIPT_DIR/:/root/ros2_ws/src/py_roomba_adapter_ros2/" \
  --name=py_roomba_adapter_ros2_container \
  $IMAGE_NAME \
  bash
