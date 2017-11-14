http://wiki.ros.org/kinetic/Installation/Ubuntu

# 在VMware虚拟机中全新安装的Ubuntu 16.04 里安装 ROS-kinetic

- 安装VMware Fusion 最新版(my is 专业版 8.5.7 (5528452))
- 在VMware虚拟机里安装Ubuntu 16.04
- sudo apt-get update
- 必须！ sudo apt-get upgrade
- sudo apt-get install vim
- sudo apt-get install openssh-server
- sudo reboot 

- ls /etc/apt/sources.list.d/
- sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros-latest.list'
- sudo vi /etc/apt/sources.list.d/ros-latest.list
- wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
- 在安装之前要清理一下，不然安装不能通过
- sudo apt-get clean
- sudo apt-get autoclean
- ls /var/lib/apt/lists/
- sudo rm -rf /var/lib/apt/lists/*
- sudo apt-get update
- sudo apt-get install ros-kinetic-desktop-full
- sudo apt-get install ros-kinetic-desktop
- sudo apt-get install ros-kinetic-ros-base
- apt-cache search ros-kinetic
- 初始化 ROS
- sudo rosdep init
- ping raw.githubusercontent.com
- rosdep update #这里要从GitHub下载配置文件，网络差
- echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
- sudo apt-get install python-rosinstall
- sudo reboot 
- 完成安装。