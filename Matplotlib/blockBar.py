#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Evan on 2019/9/30

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'

nameList = ['语文', '数学', '英语']
c1 = [81.4, 83, 81.1]
c2 = [85.6, 87.4, 90]
c3 = [78, 81.2, 86.1]

width = 0.4
x = [1, 3, 5]

plt.bar(x, c1, label='一班', fc='r', width=width)

x = [1.4, 3.4, 5.4]
plt.bar(x, c2, label='二班', fc='g', width=width)
plt.xticks(x, nameList)

x = [1.8, 3.8, 5.8]
plt.bar(x, c3, label='三班', fc='b', width=width)

plt.legend()
plt.title("三个班级成绩图")
plt.xlabel("学科")
plt.ylabel("成绩")
plt.show()