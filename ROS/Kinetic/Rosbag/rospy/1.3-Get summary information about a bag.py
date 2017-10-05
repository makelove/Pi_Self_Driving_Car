# -*- coding: utf-8 -*-
# @Time    : 2017/10/5 10:48
# @Author  : play4fun
# @File    : 1.3-Get summary information about a bag.py
# @Software: PyCharm

"""
1.3-Get summary information about a bag.py:
"""

import subprocess, yaml

info_dict = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', 'input.bag'], stdout=subprocess.PIPE).communicate()[0])

#相同地
import yaml
from rosbag.bag import Bag

info_dict = yaml.load(Bag('input.bag', 'r')._get_yaml_info())