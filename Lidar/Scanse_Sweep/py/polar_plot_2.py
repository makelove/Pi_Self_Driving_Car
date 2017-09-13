# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 11:20
# @Author  : play4fun
# @File    : polar_plot_2.py
# @Software: PyCharm

"""
polar_plot_2.py:
"""

import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0, 2 * np.pi, 0.02)

plt.subplot(121, polar=True)
plt.plot(theta, 2 * np.ones_like(theta), lw=2)
plt.plot(theta, theta / 6, '--', lw=2)

plt.subplot(122, polar=True)
plt.plot(theta, np.cos(5 * theta), '--', lw=2)
plt.plot(theta, 2 * np.cos(4 * theta), lw=2)

plt.rgrids(np.arange(0.5, 2, 0.5), angle=45)
plt.thetagrids([0, 45, 90])

plt.show()
