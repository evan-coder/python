#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Evan on 2019/9/26

import matplotlib.pyplot as plt
import matplotlib as mpl

heights = [168, 155, 182, 170, 173, 161, 155, 173, 176, 181, 166, 172, 170]
bins = range(150, 195, 5)

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel("身高")
plt.ylabel("数量")
plt.hist(heights, bins=bins)
plt.show()