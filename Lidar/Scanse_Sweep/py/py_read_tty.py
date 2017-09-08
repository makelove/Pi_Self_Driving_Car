# -*- coding: utf-8 -*-
# @Time    : 2017/9/8 09:58
# @Author  : play4fun
# @File    : py_read_tty.py
# @Software: PyCharm

"""
py_read_tty.py:
http://blog.pistuffing.co.uk/first-contact/
"""

import serial

# sweep = serial.Serial("/dev/ttyUSB0",
sweep = serial.Serial("/dev/tty.usbserial-DM00KZW7",
                      baudrate=115200,
                      parity=serial.PARITY_NONE,
                      bytesize=serial.EIGHTBITS,
                      stopbits=serial.STOPBITS_ONE,
                      xonxoff=False,
                      rtscts=False,
                      dsrdtr=False)
print("Scanse Sweep open")
sweep.write(b"ID\n")
print("Version requested")
resp = sweep.readline()
print("Response: ", resp)#Response:  b'ID115200110050500\n'
