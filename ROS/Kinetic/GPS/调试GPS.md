在ROS中调试GPS ublox-7N

### 安装驱动
- http://wiki.ros.org/nmea_gps_driver
- https://github.com/ros-drivers/nmea_gps_driver
- 把它git clone 到catkin_ws/src/然后在到catkin_ws目录catkin_make

#### 调试
- sudo chmod 777 /dev/ttyACM0

- rosrun nmea_gps_driver nmea_gps_driver.py  _port:=/dev/ttyACM0 _baud:=9600

- rostopic echo /fix
- rostopic echo /fix/latitude
#### 读取GPS模块输出
- screen /dev/ttyACM0 9600

### ublox GPS模块
http://wiki.ros.org/ublox
https://github.com/KumarRobotics/ublox