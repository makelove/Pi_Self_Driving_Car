# 在树莓派3b安装ROS-Kinetic
http://wiki.ros.org/kinetic/Installation/Ubuntu

- sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
- sudo apt install dirmngr
- sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
- sudo apt-get update