#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Evan on 2019/9/28

import matplotlib.pyplot as plt

# 极径
r = [1, 2, 3, 4, 5]

theta = [0.0, 1.5707963267948966, 3.141592653589793, 4.71238898038469, 6.283185307179586]

ax = plt.subplot(111, projection='polar').plot(theta, r)
plt.show()
