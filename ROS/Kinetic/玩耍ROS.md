# play with ROS kinetic

- echo $ROS_PACKAGE_PATH
- mkdir –p ~/dev/catkin_ws/src
- cd dev/catkin_ws/src/
- ls
- catkin_init_workspace
- cd ~/dev/catkin_ws
- catkin_make
- echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
- cd ~/dev/catkin_ws/src
- catkin_create_pkg chapter2_tutorials std_msgs roscpp
- cd ~/dev/catkin_ws/
- catkin_make
- roscd chapter2_tutorials/
- git
- git clone https://github.com/PacktPublishing/Effective-Robotics-Programming-with-ROS.git
- ls
- sudo apt-get install ros-kinetic-ros-tutorials
- roscore
- rosnode
- rosnode list
- rosnode info
- rosnode info /rosout
- rosnode ping  /ros
- rosnode ping  rosout
- rosnode list
- rosnode info turtlesim
- rostopic bw -h
- rosnode list
- rosnode info teleop_turtle
- rostopic echo /turtle1/cmd_vel
- rostopic type /turtle1/cmd_vel
- rosmsg geometry_msgs/Twist
- rosmsg show geometry_msgs/Twist
- rostopic pub /turtle1/cmd_vel  geometry_msgs/Twist -r 1 -- "linear:
x: 1.0
y: 0.0
z: 0.0
angular:
x: 0.0
y: 0.0
z: 1.0"
- rosservice type /clear