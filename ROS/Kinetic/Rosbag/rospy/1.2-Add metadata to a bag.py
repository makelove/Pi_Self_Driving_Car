# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 10:48
# @Author  : play4fun
# @File    : 1.2-Add metadata to a bag.py
# @Software: PyCharm

"""
1.2-Add metadata to a bag.py:
"""

import rosbag
import rospy

with rosbag.Bag('input.bag', 'a') as bag:
    from std_msgs.msg import String
    metadata_msg = String(data='my metadata')
    bag.write('/metadata', metadata_msg, rospy.Time(bag.get_end_time()))

