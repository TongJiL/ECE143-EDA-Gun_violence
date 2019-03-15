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


gun = pd.read_csv('gun-violence-data_01-2013_03-2018.csv')

gun_choice = gun[gun['state'].isin(['California','Texas','Missouri','Ohio','Illinois','Michigan','Tennessee','Pennsylvania','Louisiana','New York'])]

gun_choice['date'] = pd.to_datetime(gun_choice['date'])

dt = gun_choice.set_index('date')

'''................2013-2018...............'''
# statistic by years from 2013-1028

dt_1318 = dt['2013':'2016']
gun_year = dt_1318.resample('A').mean()
gun_year['victim'] = gun_year['n_killed']+gun_year['n_injured']

'''.............2014................'''
#normalize the data of 2014
dt = gun_choice.set_index('date')
year_14 = dt['2014']

state_14 = year_14.groupby(year_14['state']).sum()

state_14['victim'] = state_14['n_killed']+state_14['n_injured']

state_14['victim'].plot.bar()
plt.show()

gun_14 = list(state_14['victim'])
norm_gun14 = norm(np.array(gun_14)).reshape(10,1)

#
'''.............2015................'''
#normalize the data of 2015

year_15 = dt['2015']

state_15 = year_15.groupby(year_15['state']).sum()

state_15['victim'] = state_15['n_killed']+state_15['n_injured']

state_15['victim'].plot.bar()
plt.show()

gun_15 = list(state_15['victim'])
norm_gun15 = norm(np.array(gun_15)).reshape(10,1)
#
'''.............2016................'''
#normalize the data of 2016

year_16 = dt['2016']

state_16 = year_16.groupby(year_16['state']).sum()

state_16['victim'] = state_16['n_killed']+state_16['n_injured']

state_16['victim'].plot.bar()
plt.show()

gun_16 = list(state_16['victim'])
norm_gun16 = norm(np.array(gun_16)).reshape(10,1)
#
#

'''............write the normalize data into files...........'''
norm_gun = np.hstack([norm_gun14,norm_gun15,norm_gun16])

state = [['California'],['Illinois'],['Louisiana'],['Michigan'],['Missouri'],['New York'],['Ohio'],['Pennsylvania'],['Tennessee'],['Texas']]

with open("normgun.csv","w",newline='') as csvfile: 
    writer = csv.writer(csvfile)

    writer.writerows(zip(state,norm_gun))


    
















