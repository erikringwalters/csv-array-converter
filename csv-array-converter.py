# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:54:39 2019

@author: Erik
"""

import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/Erik/Downloads/user_infraction.csv", header=0, parse_dates=[0], index_col=0)
data
npDat = data.values
npDat = npDat.reshape(1,4000)
npDat
npDat.tofile("np_user_infraction.txt", sep=',', format='%s')

data2 = pd.read_csv("C:/Users/Erik/Downloads/sent_out_company.csv", header=0, parse_dates=[0], index_col=0)
data2
npDat2 = data2.values
npDat2 = npDat2.reshape(1,4000)
npDat2
npDat2.tofile("np_sent_out_company.txt", sep=',', format='%s')

data3 = pd.read_csv("C:/Users/Erik/Downloads/rec_out_company.csv", header=0, parse_dates=[0], index_col=0)
data3
npDat3 = data3.values
npDat3 = npDat3.reshape(1,4000)
npDat3
npDat3.tofile("np_rec_out_company.txt", sep=',', format='%s')

data4 = pd.read_csv("C:/Users/Erik/file_copy.csv", header=0, parse_dates=[0], index_col=0)