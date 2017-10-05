# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 10:47
# @Author  : play4fun
# @File    : 1.1-Rewrite bag with header timestamps.py
# @Software: PyCharm

"""
1.1-Rewrite bag with header timestamps.py:

http://wiki.ros.org/rosbag/Cookbook

"""

import rosbag

with rosbag.Bag('output.bag', 'w') as outbag:
    for topic, msg, t in rosbag.Bag('input.bag').read_messages():
        # This also replaces tf timestamps under the assumption
        # that all transforms in the message share the same timestamp
        if topic == "/tf" and msg.transforms:
            outbag.write(topic, msg, msg.transforms[0].header.stamp)
        else:
            outbag.write(topic, msg, msg.header.stamp if msg._has_header else t)