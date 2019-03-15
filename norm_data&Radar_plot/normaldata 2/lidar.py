#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:34:21 2019

@author: luodi
"""
'''
Compute the pearson correlation coeffcient rate
Plot the Radar plot of the normalize data of 2014-2016
Data contains:
    Normalized Crime rate
    Normalized Suicide rate
    Normalized Unemployment rate
    Normalized Weapon hold
    Normalized Mental health
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def cof(X1,Y1):
    '''
    pearson coeffcient rate
    input: X1, Y1
    type: pandas.core.series.Series
    output type: float
    '''
    assert isinstance(X1,pd.core.series.Series)
    assert isinstance(Y1,pd.core.series.Series)
    cof = X1.corr(Y1,method="pearson")
    return cof


if __name__ == '__main__':
    
    '''...................2014......................'''
    
    normcrim14 = pd.read_csv('2014normCrime.csv')
    X1 = pd.Series(normcrim14['crime rate'])
    Y1 = pd.Series(normcrim14['number of casualty'])
    cof_crim14 = abs(cof(X1,Y1))
    
    normemp14 = pd.read_csv('2014normEmpl.csv')
    X1 = pd.Series(normemp14['unemployment rate'])
    Y1 = pd.Series(normemp14['number of casualty'])
    cof_emp14 = abs(cof(X1,Y1))
    
    normwep14 = pd.read_csv('2014normNumRegWeap.csv')
    X1 = pd.Series(normwep14['number of registered guns'])
    Y1 = pd.Series(normemp14['number of casualty'])
    cof_wep14 = abs(cof(X1,Y1))
    
    normsuic14 = pd.read_csv('2014normSuic.csv')
    X1 = pd.Series(normsuic14['suicide rate'])
    Y1 = pd.Series(normsuic14['number of casualty'])
    cof_suic14 = abs(cof(X1,Y1))
    
    #normmh14 = pd.read_csv('norm_mh2014.csv')
    normmh14 = pd.read_csv('2014mental.csv')
    #X1 = pd.Series(normmh14['yes_1'])
    X1 = pd.Series(normmh14['number of mentally illed patients'])
    Y1 = pd.Series(normsuic14['number of casualty'])
    cof_mh14 = abs(cof(X1,Y1))
    
    '''....................Radar 2014...................'''
    # plot the Radar plot of 2014
    labels = np.array([u'Crime rate', u'Unemployment', u'Suicide rate',u'Mental health',u'Weapon hold'])
    dataLenth = 5
    data_radar = np.array([cof_crim14, cof_emp14, cof_suic14, cof_mh14, cof_wep14])
    angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
    data_radar = np.concatenate((data_radar, [data_radar[0]]))  
    angles = np.concatenate((angles, [angles[0]]))  
    plt.polar(angles, data_radar, 'bo-', linewidth=1)
    plt.thetagrids(angles * 180/np.pi, labels)  
    plt.fill(angles, data_radar, facecolor='r', alpha=0.25)
    plt.ylim(0, 1)
    plt.title('Radar plot for Cof 2014',y=1.1)
    plt.show()
    
    
    
    
    '''...................2015......................'''
    
    normcrim15 = pd.read_csv('2015normCrime.csv')
    X1 = pd.Series(normcrim15['crime rate'])
    Y1 = pd.Series(normcrim15['number of casualty'])
    cof_crim15 = abs(cof(X1,Y1))
    
    normemp15 = pd.read_csv('2015normEmpl.csv')
    X1 = pd.Series(normemp15['unemployment rate'])
    Y1 = pd.Series(normemp15['number of casualty'])
    cof_emp15 = abs(cof(X1,Y1))
    
    normwep15 = pd.read_csv('2015normNumRegWeap.csv')
    X1 = pd.Series(normwep15['number of registered guns'])
    Y1 = pd.Series(normemp15['number of casualty'])
    cof_wep15 = abs(cof(X1,Y1))
    
    normsuic15 = pd.read_csv('2015normSuic.csv')
    X1 = pd.Series(normsuic15['suicide rate'])
    Y1 = pd.Series(normsuic15['number of casualty'])
    cof_suic15 = abs(cof(X1,Y1))
    
    normmh15 = pd.read_csv('2014mental.csv')
    #X1 = pd.Series(normmh14['yes_1'])
    X1 = pd.Series(normmh15['number of mentally illed patients'])
    Y1 = pd.Series(normsuic15['number of casualty'])
    cof_mh15 = abs(cof(X1,Y1))
    
    '''....................Radar 2015...................'''
    # plot the Radar plot of 2015
    labels = np.array([u'Crime rate', u'Unemployment', u'Suicide rate',u'Mental health',u'Weapon hold'])
    dataLenth = 5
    data_radar = np.array([cof_crim15, cof_emp15, cof_suic15, cof_mh15, cof_wep15])
    angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
    data_radar = np.concatenate((data_radar, [data_radar[0]]))  
    angles = np.concatenate((angles, [angles[0]]))  
    plt.polar(angles, data_radar, 'bo-', linewidth=1)  
    plt.thetagrids(angles * 180/np.pi, labels)  
    plt.fill(angles, data_radar, facecolor='r', alpha=0.25)
    plt.ylim(0, 1)
    plt.title('Radar plot for Cof 2015',y=1.1)
    plt.show()
    
    
    
    '''...................2016......................'''
    
    normcrim16 = pd.read_csv('2016normCrime.csv')
    X1 = pd.Series(normcrim16['crime rate'])
    Y1 = pd.Series(normcrim16['number of casualty'])
    cof_crim16 = abs(cof(X1,Y1))
    
    normemp16 = pd.read_csv('2016normEmpl.csv')
    X1 = pd.Series(normemp16['unemployment rate'])
    Y1 = pd.Series(normemp16['number of casualty'])
    cof_emp16 = abs(cof(X1,Y1))
    
    normwep16 = pd.read_csv('2016normNumRegWeap.csv')
    X1 = pd.Series(normwep16['number of registered guns'])
    Y1 = pd.Series(normemp16['number of casualty'])
    cof_wep16 = abs(cof(X1,Y1))
    
    normsuic16 = pd.read_csv('2016normSuic.csv')
    X1 = pd.Series(normsuic16['suicide rate'])
    Y1 = pd.Series(normsuic16['number of casualty'])
    cof_suic16 = abs(cof(X1,Y1))
    
    #normmh16 = pd.read_csv('norm_mh2016.csv')
    normmh16 = pd.read_csv('2014mental.csv')
    #X1 = pd.Series(normmh16['yes_2'])
    X1 = pd.Series(normmh16['number of mentally illed patients'])
    Y1 = pd.Series(normsuic16['number of casualty'])
    cof_mh16 = abs(cof(X1,Y1))
    
    '''....................Radar 2016...................'''
    # plot the Radar plot of 2014
    labels = np.array([u'Crime rate', u'Unemployment', u'Suicide rate',u'Mental health',u'Weapon hold'])
    dataLenth = 5
    data_radar = np.array([cof_crim16, cof_emp16, cof_suic16, cof_mh16, cof_wep16])
    angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
    data_radar = np.concatenate((data_radar, [data_radar[0]]))
    angles = np.concatenate((angles, [angles[0]]))  
    plt.polar(angles, data_radar, 'bo-', linewidth=1)  
    plt.thetagrids(angles * 180/np.pi, labels)  
    plt.fill(angles, data_radar, facecolor='r', alpha=0.25)
    plt.ylim(0, 1)
    plt.title('Radar plot for Cof 2016',y=1.1)
    plt.show()
