# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 10:49
# @Author  : play4fun
# @File    : 1.4-Get lists of topics and types from a bag.py
# @Software: PyCharm

"""
1.4-Get lists of topics and types from a bag.py:
"""

import rosbag
bag = rosbag.Bag('input.bag')
topics = bag.get_type_and_topic_info()[1].keys()
types = []
for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
    types.append(bag.get_type_and_topic_info()[1].values()[i][0])