## 怎样播放Lidar数据-重现扫描过程
- roscore
- rosbag play -l --clock Lecture3SLAM_Tutorial.bag
- rosrun rviz rviz 
	- 添加LaserScan
	- 修改FixedFrame为laser
	- 便能显示：激光扫描的动态过程
