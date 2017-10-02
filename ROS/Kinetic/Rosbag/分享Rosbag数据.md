#分享Rosbag数据
- GPS
	- 本人使用ublox 7N模块，户外测试
- 激光雷达
- IMU
	- 数据不太好
- SLAM
	- rosbag play -l --clock Lecture3SLAM_Tutorial.bag  


## 怎样播放
- 查看帮助文档 rosbag play -h
- 循环播放 rosbag play --loop
- 播放速率 rosbag play --rate=0.5 
- 实时时钟 rosbag play --clock

## 技巧
- 查看topic rostopic list
- 查看某节点发布的topic :rosnode info rosout