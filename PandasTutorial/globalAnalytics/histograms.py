#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:00:06 2022

@author: nick
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_csv(
    '/users/nick/programming/the_algorithms/PandasTutorial/globalAnalytics/data/Population_of_Countries.csv',
    low_memory=False, encoding='cp1252'
)

plt.hist(df['2019'])
plt.show()

df['2019_mln'] = df['2019'] / 1000000
plt.hist(df['2019_mln'], range=(0, 100), bins=20)
# (100 - 0) / 20 = 5

plt.hist(df['2019_mln'], range=(0, 100), bins=20, alpha=0.5, color='red')

Europe = df[df.Region == 'Europe & Central Asia']
Africa = df[df.Region == 'Sub-Saharan Africa']


fig, axs = plt.subplots(1,2, sharey=True, tight_layout=True)

axs[0].hist(
    Europe['2019_mln'], range=(1, 210), bins=21, alpha=0.5, 
    color='red', histtype='step', linewidth=3
)
axs[1].hist(
    Africa['2019_mln'], range=(1, 210), bins=21, alpha=0.5, 
    color='blue', histtype='step', linewidth=3
)

#plt.savefig('./my_histogram.png')
