#!/opt/homebrew/bin python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:13:38 2023

@author: Prytula Mykola 124m-22-1
"""

# https://youtu.be/-sJxwvx0P20

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('loan_applic.csv')

#print(df.head(20))
info = df.info()
desc = df.describe()
shape = df.shape
cols = df.columns
types = df.dtypes

plt.plot(df['customer Age'])

