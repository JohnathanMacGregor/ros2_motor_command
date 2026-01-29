#!/usr/bin/env python 3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MotorCmdPublisher(Node):
    def __init__(self):
        super().__init__("motor_cmd_publisher")
        self.publisher_ = self.create_publisher(Twist, "/motor_cmd",10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.t = 0
        self.get_logger().info("Motor command publisher started")

    
    def timer_callback(self):
        msg = Twist()

        msg.linear.x = 0.2 + 0.05 * (self.t % 5)
        msg.angular.z = 0.5 if (self.t % 10) < 5 else -0.5

        self.publisher_.publish(msg)
        self.get_logger().info("Publishing linear.x: " + str(msg.linear.x) +
        " , angular.z: " + str(msg.angular.z))

        self.t += 1

def main(args=None):
    rclpy.init(args=args)
    node = MotorCmdPublisher()
    rclpy.spin(node)
    rclpy.shutdown()