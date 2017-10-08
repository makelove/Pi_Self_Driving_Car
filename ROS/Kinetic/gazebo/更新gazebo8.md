## 更新Gazebo 8
- 参考链接:[在ROS Kinetic中使用Gazebo 8进行机器人仿真](http://blog.csdn.net/zhangrelay/article/details/74356137)
- [官方指南](http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install)

## 步骤
- sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
- wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
- sudo apt-get update
- apt-cache search Kinetic-gazebo8
- install
