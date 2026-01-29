#!/usr/bin/env python 3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MotorCmdSubscriber(Node):
    def __init__(self):
        super().__init__("motor_cmd_subscriber")
        self.subscription = self.create_subscription(
            Twist, "/motor_cmd", self.listener_callback, 10
        )
        self.get_logger().info("Motor command subscriber started")

    def listener_callback(self, msg):
        self.get_logger().info("Received linear.x: " + str(msg.linear.x) + 
                               " , angular.z: " + str(msg.angular.z))
        
def main(args=None):
    rclpy.init(args=args)
    node = MotorCmdSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()