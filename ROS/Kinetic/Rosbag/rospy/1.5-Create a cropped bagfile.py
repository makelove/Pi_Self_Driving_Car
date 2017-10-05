# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 10:50
# @Author  : play4fun
# @File    : 1.5-Create a cropped bagfile.py
# @Software: PyCharm

"""
1.5-Create a cropped bagfile.py:
"""

import rosbag

num_msgs = 100

with rosbag.Bag('output.bag', 'w') as outbag:
    for topic, msg, t in rosbag.Bag('input.bag').read_messages():
        if num_msgs < 1:
            break
        num_msgs -= 1
        outbag.write(topic, msg, t)