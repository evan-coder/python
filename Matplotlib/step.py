#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Evan on 2019/9/28

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]

# 时间 年份
year = range(2005, 2020)
print(len(list(year)))

# 身高
height = [157, 160, 162, 163, 167, 170, 173, 175, 174, 179, 182, 182, 182, 182, 183]
print(len(height))
plt.step(year, height)
plt.show()
