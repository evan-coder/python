#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Evan on 2019/9/26

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

data = [77, 70, 72, 89, 89, 70, 90, 87, 94, 80, 95, 67, 65, 88, 60, 67, 85, 88, 87, 75, 62, 65, 95, 62, 61, 93, 30]

plt.boxplot(data)
plt.show()