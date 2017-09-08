# -*- coding: utf-8 -*-
# @Time    : 2017/9/8 11:43
# @Author  : play4fun
# @File    : scan_write_csv.py
# @Software: PyCharm

"""
scan_write_csv.py:把点云写入csv，然后在Sweep Visualizer观看
"""

from sweeppy import Sweep, Sample
import csv
from time import time,sleep


def write_csv(scans):
    filename = 'one_sample3.csv'
    headers = ['TIMESTAMP', 'AZIMUTH', 'DISTANCE', 'SIGNAL_STRENGTH']
    with open(filename, 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        for scan in scans:
            for i, sample in enumerate(scan.samples):
                # sample: Sample
                if i == 0:
                    row = [int(time() * 1000), sample.angle/1000, sample.distance, sample.signal_strength]
                else:
                    row = [-1, sample.angle/1000, sample.distance, sample.signal_strength]
                f_csv.writerow(row)


from itertools import islice

if __name__ == '__main__':
    # with Sweep('/dev/ttyUSB0') as sweep:
    with Sweep('/dev/tty.usbserial-DM00KZW7') as sweep:
        print('start_scanning')
        sweep.start_scanning()
        print('sleep(5)')
        sleep(2)
        scan1 = sweep.get_scans()
        # scan = scan1.__next__()
        # for scan in islice(sweep.get_scans(), 3):
        #
        # write_csv(scan)
        # scans = list(islice(sweep.get_scans(), 10))
        scans = []
        for x in range(0, 21):
            scan = scan1.__next__()
            scans.append(scan)
        write_csv(scans)

        print('stop_scanning')
        sweep.stop_scanning()
        sweep.set_motor_speed(0)
