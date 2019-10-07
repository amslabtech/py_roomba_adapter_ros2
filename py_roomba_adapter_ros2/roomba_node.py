#!/usr/bin/env python
#! coding: utf-8

import os

import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from std_msgs.msg import String

class RoombaNode(Node):
    def __init__(self):
        super().__init__('roomba_node')

    def _callback(self, msg):
        print('callback')

def main(args=None):
    rclpy.init(args=args)

    node = RoombaNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
