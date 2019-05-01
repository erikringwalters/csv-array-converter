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

data4 = pd.read_csv("C:/Users/Erik/csv-array-converter/file_copy.csv", header=0, parse_dates=[0], index_col=0)
data4
npDat4 = data4.values
npDat4
media_user = data4.values
npDat4[:,0]
to_media = npDat4[:,0].reshape(1,788)
from_media = npDat4[:,1].reshape(1,788)
to_media
from_media
to_media.tofile("to_media.json", sep=',', format='%s')
from_media.tofile("from_media.json", sep=',', format='%s')

to_media[np.isnan(from_media)]

d = pd.read_csv("C:/Users/Erik/csv-array-converter/all_dfs.csv", header=0, parse_dates=[0], index_col=0)
dnonan = d[np.isfinite(d['to_removable_media'])]

npD = dnonan.values
#npD = npD.reshape(9, 785)
user = npD[:,0] # user
to_rem = npD[:,1] # to_rem
from_rem = npD[:,2] # from_rem
ins_threat = npD[:,8]

user_true = user[ins_threat == True]
to_rem_true = to_rem[ins_threat == True]
from_rem_true = from_rem[ins_threat == True]

user_false = user[ins_threat == False]
to_rem_false = to_rem[ins_threat == False]
from_rem_false = from_rem[ins_threat == False]

user_true.tofile("user_true.txt", sep=',', format='%s')
to_rem_true.tofile("to_rem_true.txt", sep=',', format='%s')
from_rem_true.tofile("from_rem_true.txt", sep=',', format='%s')

user_false.tofile("user_false.txt", sep=',', format='%s')
to_rem_false.tofile("to_rem_false.txt", sep=',', format='%s')
from_rem_false.tofile("from_rem_false.txt", sep=',', format='%s')

#-----rec_out sent_out --------
d2 = pd.read_csv("C:/Users/Erik/Downloads/all_dfs.csv", header=0, parse_dates=[0], index_col=0)

npD2 = d2[d2['rec_out'] > 0].values

user = npD2[:,0]
rec_out = npD2[:,1]
sent_out = npD2[:,2]
ins_threat = npD2[:,8]

user_true = user[ins_threat == True]
rec_out_true = rec_out[ins_threat == True]
sent_out_true = sent_out[ins_threat == True]

user_false = user[ins_threat == False]
rec_out_false = rec_out[ins_threat == False]
sent_out_false = sent_out[ins_threat == False]

user_true.tofile("user_true.txt", sep=',', format='%s')
rec_out_true.tofile("rec_out_true.txt", sep=',', format='%s')
sent_out_true.tofile("sent_out_true.txt", sep=',', format='%s')

user_false.tofile("user_false.txt", sep=',', format='%s')
rec_out_false.tofile("rec_out_false.txt", sep=',', format='%s')
sent_out_false.tofile("sent_out_false.txt", sep=',', format='%s')

npd3 = d2.values

user = npd3[:,0]
logoff = npd3[:,6]
logon = npd3[:,7]
ins_threat = npd3[:,8]

user_true = user[ins_threat == True]
logoff_true = logoff[ins_threat == True]
logon_true = logon[ins_threat == True]


user_false = user[ins_threat == False]
logoff_false = logoff[ins_threat == False]
logon_false = logon[ins_threat == False]


user_true.tofile("user_true.json", sep='","', format='%s')
logoff_true.tofile("logoff_true.json", sep=',', format='%s')
logon_true.tofile("logon_true.json", sep=',', format='%s')

user_false.tofile("user_false.json", sep='","', format='%s')
logoff_false.tofile("logoff_false.json", sep=',', format='%s')
logon_false.tofile("logon_false.json", sep=',', format='%s')
