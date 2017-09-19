### 安装
- sudo apt-get install ros-kinetic-usb-cam
### 运行
- roslaunch usb_cam usb_cam-test.launch 
- 订阅 rosrun image_view image_view image:=/usb_cam/image_raw
便看到摄像头的画面
- rostopic list


### 使用OpenCV
http://www.ncnynl.com/archives/201611/1067.html
- rosrun beginner_tutorials subscriber_publisher_CompressedImage.py