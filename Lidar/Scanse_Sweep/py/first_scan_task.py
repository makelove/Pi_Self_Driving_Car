# -*- coding: utf-8 -*-
# @Time    : 2017/9/7 10:02
# @Author  : play4fun
# @File    : te1.py
# @Software: PyCharm

"""
te1.py:
"""

from sweeppy import Sweep,Scan,Sample

# with Sweep('/dev/ttyUSB0') as sweep:
with Sweep('/dev/tty.usbserial-DM00KZW7') as sweep:
    print('start_scanning')
    sweep.start_scanning()
    try:
        for scan in sweep.get_scans():
            print('{}\n'.format(scan))
            #
            # scan = Scan()
            # scan.samples
            sam = Sample()
            # sam.angle
            # sam.distance
            # sam.signal_strength
            sam.
            print('len(scan.samples):',len(scan.samples))
    except KeyboardInterrupt as e:
        print(e, 'Stop scanning')
        sweep.stop_scanning()
    finally:
        sweep.set_motor_speed(0)

# 正常工作！

'''
#run at  ipython
from sweeppy import Sweep
with Sweep('/dev/ttyUSB0') as sweep:
    print('start_scanning')
    sweep.start_scanning()
    scan1 = sweep.get_scans()
    scan=scan1.__next__()
    sweep.stop_scanning()
    sweep.set_motor_speed(0)

'''
