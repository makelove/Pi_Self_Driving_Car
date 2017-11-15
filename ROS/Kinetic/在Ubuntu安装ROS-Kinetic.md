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
    - 早上的网络好，干扰少
    - 重复执行，直到成功为止
        - for i in {1..10};do rosdep update;sleep 10; done
- echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
- sudo apt-get install python-rosinstall
- sudo reboot 
- 完成安装。


## 常用包
```bash
sudo apt-get install ros-kinetic-amcl:amd64 ros-kinetic-assimp-devel:amd64 ros-kinetic-astra-camera:amd64 ros-kinetic-astra-launch:amd64 ros-kinetic-audio-common-msgs:amd64 ros-kinetic-base-local-planner:amd64 ros-kinetic-bfl:amd64 ros-kinetic-camera-calibration:amd64 ros-kinetic-capabilities:amd64 ros-kinetic-clear-costmap-recovery:amd64 ros-kinetic-compressed-depth-image-transport:amd64 ros-kinetic-compressed-image-transport:amd64 ros-kinetic-costmap-2d:amd64 ros-kinetic-create-description:amd64 ros-kinetic-create-driver:amd64 ros-kinetic-create-node:amd64 ros-kinetic-depthimage-to-laserscan:amd64 ros-kinetic-desktop-full:amd64 ros-kinetic-diff-drive-controller:amd64 ros-kinetic-dwa-local-planner:amd64 ros-kinetic-dynamic-tf-publisher:amd64 ros-kinetic-ecl-build:amd64 ros-kinetic-ecl-command-line:amd64 ros-kinetic-ecl-concepts:amd64 ros-kinetic-ecl-config:amd64 ros-kinetic-ecl-containers:amd64 ros-kinetic-ecl-converters:amd64 ros-kinetic-ecl-devices:amd64 ros-kinetic-ecl-eigen:amd64 ros-kinetic-ecl-errors:amd64 ros-kinetic-ecl-exceptions:amd64 ros-kinetic-ecl-formatters:amd64 ros-kinetic-ecl-geometry:amd64 ros-kinetic-ecl-license:amd64 ros-kinetic-ecl-linear-algebra:amd64 ros-kinetic-ecl-math:amd64 ros-kinetic-ecl-mobile-robot:amd64 ros-kinetic-ecl-mpl:amd64 ros-kinetic-ecl-sigslots:amd64 ros-kinetic-ecl-streams:amd64 ros-kinetic-ecl-threads:amd64 ros-kinetic-ecl-time:amd64 ros-kinetic-ecl-time-lite:amd64 ros-kinetic-ecl-type-traits:amd64 ros-kinetic-ecl-utilities:amd64 ros-kinetic-euscollada:amd64 ros-kinetic-euslisp:amd64 ros-kinetic-forward-command-controller:amd64 ros-kinetic-freenect-camera:amd64 ros-kinetic-freenect-launch:amd64 ros-kinetic-freenect-stack:amd64 ros-kinetic-gateway-msgs:amd64  ros-kinetic-gazebo-dev:amd64 ros-kinetic-gazebo-msgs:amd64 ros-kinetic-gazebo-plugins:amd64 ros-kinetic-gazebo-ros:amd64 ros-kinetic-gazebo-ros-control:amd64 ros-kinetic-gazebo-ros-pkgs:amd64 ros-kinetic-gps-common:amd64 ros-kinetic-gpsd-client:amd64 ros-kinetic-gps-umd:amd64 ros-kinetic-gscam:amd64 ros-kinetic-image-common:amd64 ros-kinetic-image-pipeline:amd64 ros-kinetic-image-publisher:amd64 ros-kinetic-image-rotate:amd64 ros-kinetic-image-transport-plugins:amd64 ros-kinetic-image-view2:amd64 ros-kinetic-imu-complementary-filter:amd64 ros-kinetic-imu-filter-madgwick:amd64 ros-kinetic-jsk-data:amd64 ros-kinetic-jskeus:amd64 ros-kinetic-jsk-footstep-msgs:amd64 ros-kinetic-jsk-pcl-ros:amd64 ros-kinetic-jsk-pcl-ros-utils:amd64 ros-kinetic-jsk-recognition-msgs:amd64 ros-kinetic-jsk-recognition-utils:amd64 ros-kinetic-jsk-topic-tools:amd64 ros-kinetic-kobuki-auto-docking:amd64 ros-kinetic-kobuki-bumper2pc:amd64 ros-kinetic-kobuki-capabilities:amd64 ros-kinetic-kobuki-description:amd64 ros-kinetic-kobuki-dock-drive:amd64 ros-kinetic-kobuki-driver:amd64 ros-kinetic-kobuki-ftdi:amd64 ros-kinetic-kobuki-gazebo-plugins:amd64 ros-kinetic-kobuki-keyop:amd64 ros-kinetic-kobuki-msgs:amd64 ros-kinetic-kobuki-node:amd64 ros-kinetic-kobuki-random-walker:amd64 ros-kinetic-kobuki-rapps:amd64 ros-kinetic-kobuki-safety-controller:amd64 ros-kinetic-laptop-battery-monitor:amd64 ros-kinetic-laser-filters:amd64 ros-kinetic-laser-pipeline:amd64 ros-kinetic-libfreenect:amd64 ros-kinetic-librealsense:amd64 ros-kinetic-move-base:amd64 ros-kinetic-move-base-msgs:amd64 ros-kinetic-move-base-to-manip:amd64 ros-kinetic-nav-core:amd64 ros-kinetic-navfn:amd64 ros-kinetic-octomap-ros:amd64 ros-kinetic-octomap-server:amd64 ros-kinetic-openni2-camera:amd64 ros-kinetic-openni2-launch:amd64 ros-kinetic-openni-camera:amd64 ros-kinetic-openni-launch:amd64 ros-kinetic-perception:amd64 ros-kinetic-perception-pcl:amd64 ros-kinetic-position-controllers:amd64 ros-kinetic-pr2-common:amd64 ros-kinetic-pr2-dashboard-aggregator:amd64 ros-kinetic-pr2-description:amd64 ros-kinetic-pr2eus:amd64 ros-kinetic-pr2eus-moveit:amd64 ros-kinetic-pr2eus-tutorials:amd64 ros-kinetic-pr2-machine:amd64 ros-kinetic-pr2-msgs:amd64 ros-kinetic-razor-imu-9dof:amd64 ros-kinetic-realsense-camera:amd64 ros-kinetic-resized-image-transport:amd64 ros-kinetic-rgbd-launch:amd64 ros-kinetic-robot-pose-ekf:amd64 ros-kinetic-robot-self-filter:amd64 ros-kinetic-rocon-app-manager:amd64 ros-kinetic-rocon-app-manager-msgs:amd64 ros-kinetic-rocon-apps:amd64 ros-kinetic-rocon-app-utilities:amd64 ros-kinetic-rocon-bubble-icons:amd64 ros-kinetic-rocon-console:amd64 ros-kinetic-rocon-ebnf:amd64 ros-kinetic-rocon-gateway:amd64 ros-kinetic-rocon-gateway-utils:amd64 ros-kinetic-rocon-hub:amd64 ros-kinetic-rocon-hub-client:amd64 ros-kinetic-rocon-icons:amd64 ros-kinetic-rocon-interaction-msgs:amd64 ros-kinetic-rocon-interactions:amd64 ros-kinetic-rocon-master-info:amd64 ros-kinetic-rocon-python-comms:amd64 ros-kinetic-rocon-python-redis:amd64 ros-kinetic-rocon-python-utils:amd64 ros-kinetic-rocon-python-wifi:amd64 ros-kinetic-rocon-semantic-version:amd64 ros-kinetic-rocon-service-pair-msgs:amd64 ros-kinetic-rocon-std-msgs:amd64 ros-kinetic-rocon-uri:amd64 ros-kinetic-roseus:amd64 ros-kinetic-rosserial-server:amd64 ros-kinetic-rotate-recovery:amd64 ros-kinetic-rviz-imu-plugin:amd64 ros-kinetic-simulators:amd64 ros-kinetic-sophus:amd64 ros-kinetic-sound-play:amd64 ros-kinetic-stage:amd64 ros-kinetic-stage-ros:amd64 ros-kinetic-std-capabilities:amd64 ros-kinetic-theora-image-transport:amd64 ros-kinetic-turtlebot-bringup:amd64 ros-kinetic-turtlebot-capabilities:amd64 ros-kinetic-turtlebot-description:amd64 ros-kinetic-turtlebot-gazebo:amd64 ros-kinetic-turtlebot-navigation:amd64 ros-kinetic-turtlebot-rviz-launchers:amd64 ros-kinetic-turtlebot-teleop:amd64 ros-kinetic-unique-id:amd64 ros-kinetic-urdf-geometry-parser:amd64 ros-kinetic-urdf-sim-tutorial:amd64 ros-kinetic-urdf-tutorial:amd64 ros-kinetic-vision-opencv:amd64 ros-kinetic-voxel-grid:amd64 ros-kinetic-yocs-cmd-vel-mux:amd64 ros-kinetic-yocs-controllers:amd64 ros-kinetic-yocs-velocity-smoother:amd64 ros-kinetic-zeroconf-avahi:amd64 ros-kinetic-zeroconf-msgs:amd64
```

- gazebo8
```bash
ros-kinetic-gazebo8-msgs:amd64 ros-kinetic-gazebo8-plugins:amd64 ros-kinetic-gazebo8-ros:amd64 ros-kinetic-gazebo8-ros-control:amd64 ros-kinetic-gazebo8-ros-pkgs:amd64 
```