#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Evan on 2019/9/26

import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

data = [[18.9, 10.4], [21.3, 8.7], [19.5, 11.6], [20.5, 9.7], [19.9, 9.4], [22.3, 11], [21.4, 10.6], [9, 9.4], [10.4, 9], [9.3, 11.3], [11.6, 8.5], [11.8, 10.4], [10.3, 10], [8.7, 9.5], [14.3, 17.2], [14.1, 15.5], [14, 16.5], [16.5, 17.7], [15.1, 17.3], [16.4, 15], [15.7, 18]]

x = [item[0] for item in data]
y = [item[1] for item in data]

print(x,y)

plt.title("价位与销量散点图")
plt.xlabel("价格（元）")
plt.ylabel('销量（件）')
plt.text(15, 16, '牙膏')
plt.text(11, 10, '纸巾')
plt.text(20, 10, '洗衣液')
plt.scatter(x, y)  # 散点图
plt.show()