# motor_cmd

ROS 2 Python publisher and subscriber demonstrating motor command communication.

## Overview
This project implements a ROS 2 publisher and subscriber in Python to simulate how motor commands are sent and received in a robotics system. The publisher generates velocity commands using the `Twist` message, and the subscriber receives and logs this data. This setup models a basic control and communication pipeline used in autonomous robotic systems.

## Nodes
- **motor_cmd_publisher**  
  Publishes forward speed (`linear.x`) and turning rate (`angular.z`) values on the `/motor_cmd` topic.

- **motor_cmd_subscriber**  
  Subscribes to the `/motor_cmd` topic and logs the received motor commands.

## How to Run
```bash
colcon build
source install/setup.bash
ros2 run motor_cmd motor_cmd_pub
ros2 run motor_cmd motor_cmd_sub
