# Pi_Self_Driving_Car
- 使用树莓派3b来实现无人驾驶汽车.
    - 使用ROS把各种传感器连接起来。
    - 对动手能力要求很高。
        - 不想被折腾的朋友，建议在淘宝买现成的套餐，半成品。
        - 等熟练后，再买零件组装
        
- 路线图
    - 智能小车，组装，焊接，连接电路，使用Arduino让车动起来    
        - 智能小车底盘+电机驱动L298N+Arduino UNO R3+杜邦线+面包板+电池
    - 使用串口游戏手柄控制 智能小车 行走
    - 游戏手柄+智能小车+超声波传感器4个
    - 6轮越野小车
        - 组装，小车底盘+电机驱动MD02+Arduino UNO R3+杜邦线+面包板+电池
        - 树莓派3b，小车底盘+电机驱动MD02+Arduino UNO R3+杜邦线+面包板+电池
            - 树莓派3b<-->Arduino<-->电机驱动MD02<-->小车底盘
            - USB游戏手柄<-->树莓派3b
        - ROS
            - 树莓派3b安装Ubuntu Mate 16.04-->安装ROS kinetic
                - 建议装ROS Indigo，kinetic还有很多坑。
                - 重要是书店里的ROS图书都是基于Indigo
                - 本人是根据《ROS机器人高效编程》来学习的
            - 购买激光雷达，建议买哪款经典的RPLIDAR-A1 (升级版)
                - rviz 激光地图
                - 测速电机，里程计
                - SLAM
                    - 本人困在【hector SLAM制作地图】，小车一转弯，地图就重叠了。
            - 摄像头
                - 双目，OpenCV
                    - 视觉SLAM，困难。树莓派，运算能力差
                        - 可购买 NVIDIA Jetson TX1，TX2
                            
                - Kinect深度摄像头 
                    - 点云PCL
            - 多种传感器融合
                - 激光雷达
                - 里程计
                - 超声波传感器
                - IMU惯性导航
                - Kinect深度摄像头
        - NVIDIA Jetson TX2
            - 大杀器
            - 要配 跑车底盘，大容量电池，路由器
                - 看YouTube视频
                - 网站http://www.jetsonhacks.com/
                    - 安装，配置，优化等教程都有。
                    - 还需要更换Linux内核
            - MIT的无人驾驶课程，使用了它  
            - GPU 深度学习
        
- 参考图书
    - [ROS机器人高效编程（原书第3版）](https://item.jd.com/12169587.html)
        - 非常好的一本书！


## 开发环境
* macOS Sierra 10.12.5 
* Python 3.6.1
* OpenCV 3.2.0
* Arduino IDE 1.8.4
* ROS Kinetic
* Ubuntu 16.04

## 设备
- 智能小车
    - 舵机转向 [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.176fef06kl32WJ&id=525569912543&_u=venvdkb69a3)
    - 6WD搜救平台  [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.176fef06kl32WJ&id=541672590664&_u=venvdkb7d24)
- 树莓派3b
- Arduino UNO R3 开发板
    - Arduino Mega 2560 功能更强大！强烈推荐！
- 电机驱动
    - L298N 
    - MD02 [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.176fef06kl32WJ&id=540889441943&_u=venvdkbff0c)
- 激光雷达Scanse Sweep 40米距离 [淘宝](https://item.taobao.com/item.htm?id=545843273303&_u=t2dmg8j26111)
    - 可转让这款！请联系我。
    - 推荐[RPLIDAR-A1 (升级版)](https://item.taobao.com/item.htm?id=549730240579)
        - 很多书，很多文档都使用这款。
- 摄像头
    - 130W像素高清摄像头模组 720P 1280x720 USB2.0免驱 微距模块 [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.7f280f31zxT40g&id=17338719222&_u=venvdkbe395) 
- GPS模块
    - GPS模块 NEO-6M UBLOX 卫星定位 51单片机 Arduino STM32 例程
带有USB接口 带有SMA接口 [淘宝](https://detail.tmall.com/item.htm?id=528686611017&spm=a1z09.2.0.0.176fef06kl32WJ&_u=venvdkbb029)
- 超声波传感器 4
    - 超声波云台 带转向 固定 180 9G舵机 智能小车 测距 [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.7f280f31zxT40g&id=19789391422&_u=venvdkb5119)
- 红外线传感器+红外遥控器
- 电池 
    - 12v锂电池组聚合物太阳能路灯氙气灯10A安时大容量12000mAh  [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.7f280f31zxT40g&id=537518620774&_u=venvdkb918e) 
    - 充电宝
- 杜邦线
- IMU
    - GY-521 MPU-6050模块 三轴加速度 陀螺仪6DOF模块 [淘宝](https://item.taobao.com/item.htm?spm=a1z1r.7974869.0.0.4f1d809do5FR1k&id=537182932458) 用这个！
    - SparkFun 9DoF Razor IMU M0  ROS不支持
        - https://www.sparkfun.com/products/14001
        - 上手 https://learn.sparkfun.com/tutorials/9dof-razor-imu-m0-hookup-guide
- 游戏手柄
    - pc360/电脑PS3/安卓PS2震动usb2.4g无线游戏手柄/无延迟/街机双打 [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.7f280f31zxT40g&id=35391805818&_u=venvdkb9dc1)
- 测速电机
    - JGA25直流减速电机 带编码器 霍尔测速磁环 大扭力直流马达 [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.7f280f31zxT40g&id=45781421725&_u=venvdkb07c7)
- RGB 全彩LED   [淘宝](https://item.taobao.com/item.htm?spm=a1z09.2.0.0.7f280f31zxT40g&id=537143825494&_u=venvdkb95ff)
