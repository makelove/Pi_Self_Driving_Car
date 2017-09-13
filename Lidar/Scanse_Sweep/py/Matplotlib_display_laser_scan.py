# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 09:59
# @Author  : play4fun
# @File    : Matplotlib_display_laser_scan.py
# @Software: PyCharm

"""
Matplotlib_display_laser_scan.py:把激光雷达扫描的点云，用matplotlib显示极坐标
"""
from time import sleep
import numpy as np
# theta=np.arange(0,2*np.pi,0.02)
import matplotlib.pyplot as plt
import json

with open('one_sample1.json', 'r') as f:
# with open('/Users/play/WORK/Scanse_Sweep/docs/test11.scd', 'r') as f:
    data = json.load(f)
fig = plt.figure()
# ax1 = plt.subplot(121, projection='polar')
# ax1 = plt.subplot(111, polar=True)
ax1 = fig.add_subplot(111, polar=True)
# ax2 = plt.subplot(122)

plt.ion()
# while True:
for x in data['Sweeps']:
    angles = x['SensorReading_Angles']
    radiss = x['SensorReading_Radii']

    for angle, radis in zip(angles, radiss):
        theta = angle / 360 * np.pi * 2
        colors = theta
        print(radis, theta)
        # ax1.plot(radis, angle/360, '--', lw=2)
        ax1.scatter(theta, radis, c=colors, cmap=plt.cm.hsv)
        #         sleep(0.5)
        plt.pause(0.00001)#不能取消
        # plt.show()
        # break
    # plt.clf()
    plt.cla()
# sleep(1)
# sleep(3)
# ax2.plot(theta,theta/6,'--',lw=2)
# plt.show()
