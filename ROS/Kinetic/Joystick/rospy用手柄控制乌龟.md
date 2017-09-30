# 用手柄控制乌龟
- rospy ：https://github.com/srikanthmalla/joystick_control/blob/master/jsc.py
- joystick_node.launch
```xml
<?xml version="1.0"  ?>
<launch>
    <node respawn="true" pkg="turtlesim" type="turtlesim_node"  name="turtlesim_node"/>
    <node pkg="beginner_tutorials" type="joystick_control_turtle1.py" name="joystick_control_turtle1"/>
    <param name="axis_linear" value="1" type="int" />
    <param name="axis_angular" value="0" type="int" />
    <node respawn="true" pkg="joy" type="joy_node" name="joy_node">
        <param name="dev" type="string" value="/dev/input/js0"/>
        <param name="deadzone"  value="0.12"/>
    </node>
</launch>
```

## 参考链接
- http://wiki.ros.org/mallasrikanth/joystick%20control
- GitHub https://github.com/srikanthmalla/joystick_control
