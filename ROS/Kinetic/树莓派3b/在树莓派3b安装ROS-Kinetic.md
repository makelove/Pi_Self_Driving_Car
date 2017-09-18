# 在树莓派3b安装ROS-Kinetic
http://wiki.ros.org/kinetic/Installation/Ubuntu

- sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
- sudo apt install dirmngr
- sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
- sudo apt-get update
- sudo apt-get install ros-kinetic-desktop-full
- 不行，不支持Debian

#### 官方文档
http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi

- 下载预安装的ubuntu Mate +ROS-Kinetic 镜像
http://www.german-robot.com/2016/05/26/raspberry-pi-sd-card-image/

该图像创建于2017年2月，目前版本为Ubuntu Mate Xenial 16.04和ROS Kinetic。 用户名为“pi”，密码为“覆盆子”。 你需要一个16GB的SD卡（图像大小是8GB，一些8GB的SD卡会太小）。 [在这里下载](http://www.german-robot.com/2017-03%20Ubuntu%20Mate%2016.04%20+%20ROS%20Kinetic.img.zip) 请注意，在德语键盘上，“y”和“z”互换，因此要么切换到英文键盘，要么使用“z”代替“y”作为密码。

注意：您应在终端中输入以下内容：“nano /home/pi/.bashrc”，然后在文件末尾添加以下内容：“source /home/pi/catkin_ws/devel/setup.bash”，而不使用“” 。 然后按ctrl + x退出并保存。

设置Raspberry PI3：
使用Ubuntu Mate欢迎屏幕。 如果出现问题，请删除所有现有的Wifi-Connections。 要使用德语 - 机器人软件，请转到下面的“测试连接”一章。

测试连接

Raspberry应该运行并连接到您的Wifi网络。

为了让所有pwm通道运行，请转到PC软件（PC的Livecode程序，请参阅其他章节），单击“工具”窗口左上角的箭头，输入Robot1底部的IP地址，选择Robot1在顶部，单击“Dis- / Connect”按钮。 字段“已连接：否”应更改为“已连接：是”并保持这种方式。

如果您在“说话”并连接声音卡并连接扬声器，机器人应该开始说话。 如果声卡未连接，将出现错误信息。

为了测试伺服连接：将所有舵机连接到PCB，然后点击“校准机器人”和“分配接头编号”。 一个接一个地，当您通过程序时，每个伺服器应该开始移动。

