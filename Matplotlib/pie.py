#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Evan on 2019/9/26

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

labels = ['放贷', '饮食', '出行', '教育']
datas = [5000, 2000, 1000, 1000]

plt.pie(datas, labels=labels, autopct="%.2f%%")
plt.show()