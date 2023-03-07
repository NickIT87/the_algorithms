#!/opt/homebrew/bin python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:13:38 2023

@author: Prytula Mykola 124m-22-1
"""

import pandas as pd

df = pd.read_csv(
    '/users/nick/programming/the_algorithms/PandasTutorial/lab_project/loan_applic.csv',
    low_memory=False, encoding='cp1252'
)

#print(df.head(20))
df.info()
desc = df.describe()

