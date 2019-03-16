import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def extract_year_cas(gun_viol_path,year):
    '''
    return extracted casualty of a year in gunviolence data
    '''
    assert isinstance(year,int)
    assert isinstance(gun_viol_path,str)
    pd_gun = pd.read_csv(gun_viol_path)
    pd_gun['date'] = pd.to_datetime(pd_gun['date'])
    pd_gun['year'] = pd_gun['date'].dt.year
    a_year = pd_gun.groupby('year').get_group(year)
    b = a_year.loc[:,["state","n_killed","n_injured"]]
    b['casualty'] = b['n_killed'] + b['n_injured']
    g_count = b.groupby('state').sum()
    g_year = g_count.loc[:,['casualty']]
    gun_year = pd.DataFrame({'STATE':g_count.index,'casualty':g_year['casualty']})
    return gun_year

def merge_gun(feature_path,feature,feature_name,gun_year):
    '''
    read in feature_path and gun_year data and merge the two data
    to return dataframe of feature and casualty of a year
    '''
    assert isinstance(feature_path,str)
    assert isinstance(feature,str)
    assert isinstance(gun_year,pd.DataFrame)
    assert isinstance(feature_name,str)

    pd_feat = pd.read_csv(feature_path)
    a = pd.merge(gun_year,pd_feat, on='STATE',how='left')
    a = a.loc[:,['STATE','casualty',feature]]
    a['casualty'] = a['casualty']/a['casualty'].max()
    a[feature] = a[feature]/a[feature].max()
    a.set_index('STATE',inplace=True)
    a.sort_values(by='casualty',inplace=True)
    a.dropna(inplace=True)
    a.rename(index=str, columns={"casualty": "number of casualty", feature: feature_name},inplace=True)
    return a

def bar_gun_feature(viol_feat,feature):
    '''
    bar plot casualty vs. chosen feature in certain year and chosen states
    '''
    assert isinstance(viol_feat,pd.DataFrame)
    assert isinstance(feature,str)
    chooseState=['California','Texas','Ohio','Illinois','Michigan','Pennsylvania','Tennessee','New York','Missouri','Louisiana']
    b = viol_feat.loc[chooseState,['number of casualty',feature]]
    b.sort_values(by='number of casualty',inplace=True)
    b.index.names = ['states']
    b.plot.barh( figsize = (15,12),color=['orangered','royalblue'],fontsize=15)

def transLaw(lawPath):
    pd_law = pd.read_csv(lawPath)
    pd_law.replace({'OpenCarryAllowed_S':'yes','OpenCarryAllowed_L':'yes'},1,inplace=True)
    pd_law.replace({'OpenCarryAllowed_S':'no','OpenCarryAllowed_L':'no'},-1,inplace=True)
    pd_law.replace('yes',-1,inplace=True)
    pd_law.replace('no',1,inplace=True)
    pd_law['score'] = pd_law.sum(axis=1)
    b = pd_law.loc[:,['Unnamed: 0','score']]
    b.rename(index=str, columns={"Unnamed: 0": "STATE", 'score': 'score'},inplace=True)
    return b

if __name__ == '__main__':
    gun_year = extract_year_cas('gun-violence-data/gun-violence-data_01-2013_03-2018.csv',2014)
    mergeData = merge_gun('SUICIDE2014.csv','rate_suic','suicide rate',gun_year)
    bar_gun_feature(mergeData,'suicide rate')
    b = transLaw('gunlaw.csv')
    print(b)
