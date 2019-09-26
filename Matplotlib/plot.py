#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Evan on 2019/9/26

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.arange(1, 11)
    y = 2 * x + 5

    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.subplot(2, 1, 1)
    plt.plot(x, y, "ob")   # o - 圆形标记  b - 蓝色
    plt.title("plot training")

    x = np.arange(0, 3*np.pi, 0.1)
    y = np.sin(x)
    plt.subplot(2, 1, 2)
    plt.plot(x, y)
    plt.title("Sin")

    plt.show()