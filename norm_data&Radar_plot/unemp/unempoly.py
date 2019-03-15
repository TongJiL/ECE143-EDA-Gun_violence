#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:43:05 2019

@author: luodi

ECE 143 project
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def norm(z):
    '''
    Normalize the data into 0-1
    by divide by the largest number
    '''
    sm = z/np.max(z)
    return sm


dateparse = lambda dates: pd.datetime.strptime(dates,'%Y')
unemp = pd.read_csv('unemployment-by-county-us/output.csv',parse_dates=['Year'],\
            index_col='Year', date_parser=dateparse)
            

unemp_choice = unemp[unemp['State'].isin(['California','Texas','Missouri','Ohio','Illinois','Michigan','Tennessee','Pennsylvania','Louisiana','New York'])]


'''................2014.....................'''
year_14 = unemp_choice['2014']

ump_state_14 = year_14.groupby(year_14['State']).mean()

ump_state_14['Rate'].plot.bar()
plt.show()

unemp_14 = list(ump_state_14['Rate'])

norm_unemp14 = norm(np.array(unemp_14)).reshape(10,1)


'''................2015...............'''
year_15 = unemp_choice['2015']

ump_state_15 = year_15.groupby(year_15['State']).mean()

ump_state_15['Rate'].plot.bar()
plt.show()

unemp_15 = list(ump_state_15['Rate'])

norm_unemp15 = norm(np.array(unemp_15)).reshape(10,1)

'''................2016...............'''
year_16 = unemp_choice['2016']

ump_state_16 = year_16.groupby(year_16['State']).mean()

ump_state_16['Rate'].plot.bar()
plt.show()

unemp_16 = list(ump_state_16['Rate'])

norm_unemp16 = norm(np.array(unemp_16)).reshape(10,1)

'''............write the normalize data into files...........'''

norm_unemp = np.hstack([norm_unemp14,norm_unemp15,norm_unemp16])

state = ['California','Illinois','Louisiana','Michigan','Missouri','New York','Ohio','Pennsylvania','Tennessee','Texas']

with open("normunemp.csv","w") as csvfile: 
    writer = csv.writer(csvfile)
 
    #先写入columns_name
    writer.writerows(zip(state,norm_unemp))
#    writer.writecolumns(norm_unemp)














