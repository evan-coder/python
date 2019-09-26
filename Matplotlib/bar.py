#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Evan on 2019/9/26

from matplotlib import pyplot as plt

x = [5, 8, 10]
y = [12, 16, 6]

x2 = [6, 9, 11]
y2 = [6, 15, 7]

plt.bar(x, y, align="center")
plt.bar(x2, y2, color="g", align="center")
plt.title("Bar graph")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()