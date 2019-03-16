#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Import the required libraries 
from plotly.offline import init_notebook_mode, iplot
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from wordcloud import WordCloud
from textblob import TextBlob 
import plotly.plotly as py
from plotly import tools
import seaborn as sns
import pandas as pd
import string, os, random
import calendar
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import folium 
import plotly
from folium import plugins 
plotly.offline.init_notebook_mode(connected=True)
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
import locale

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

path = "data/gun-violence-data_01-2013_03-2018.csv"
gunIncidentsData = pd.read_csv(path)
path = "data/annual_spending.csv"
gunFundingData = pd.read_csv(path)
path = "data/gun_dollars.csv"
gunDollarsStateData = pd.read_csv(path)



# In[22]:


def gun_data_fix():
    """Get the year data and add killed+injured"""
    gunIncidentsData['date'] = pd.to_datetime(gunIncidentsData['date'])
    gunIncidentsData['year'] = gunIncidentsData['date'].dt.year
    gunIncidentsData['loss'] = gunIncidentsData['n_killed'] + gunIncidentsData['n_injured']

def create_stack_bar_data(col):
    """add this data to as 2 columns"""
    aggregated = gunIncidentsData[col].value_counts()
    x_values = aggregated.index.tolist()
    y_values = aggregated.values.tolist()
    return x_values, y_values

def nra_funding_data():
    """nra_funding_data processing"""
    gunFundingDataframe = gunFundingData[gunFundingData['Year'] > 2013]
    gunFundingDataframe.drop(columns=['Unnamed: 4', 'Unnamed: 5'])
    x2 = list(gunFundingDataframe['Gun Control'])
    x3 = list(gunFundingDataframe['Gun Rights'])
    x4 = list(gunFundingDataframe['Gun Manufacturing'])
    return(x2,x3,x4)

def gun_funding_per_state():
    """gun funding per state"""
    gunDollarsStateDataFrame = gunDollarsStateData[['Distid', 'GunControlTotal','GunRightsTotal']]
    states_id = gunDollarsStateDataFrame['Distid']
    states_id = [i[:2] for i in states_id]
    gunDollarsStateDataFrame['State'] = states_id
    gunDollarsStateDataFrame['GunControlTotal'] = [locale.atoi(n[1:]) for n in gunDollarsStateDataFrame['GunControlTotal']]
    gunDollarsStateDataFrame['GunRightsTotal'] = [locale.atoi(n[1:]) for n in gunDollarsStateDataFrame['GunRightsTotal']]
    gunDollarsStateDataFrame_temp = gunDollarsStateDataFrame.groupby(["State"], as_index=False).sum()
    gunDollarsStateDataF = gunDollarsStateDataFrame_temp.sort_values(by='State')
    return gunDollarsStateDataF
    
def sort_top_10_states(gunDollarsStateDataF):
    """sort top 10 states information"""
    gunIncidentsDataState = gunIncidentsData['state'].value_counts()
    gunIncidentsDataFrame = pd.DataFrame()
    gunIncidentsDataFrame['state'] = gunIncidentsDataState.index
    gunIncidentsDataFrame['counts'] = gunIncidentsDataState.values
    
    top_10_states = gunIncidentsDataFrame.sort_values(by='state')
    top_10_states = top_10_states.join(gunDollarsStateDataF[['GunControlTotal', 'GunRightsTotal']])
    top_10_states = top_10_states.sort_values(by='counts',ascending=False)
    top_10_states.drop(top_10_states.tail(41).index,inplace=True)
    return top_10_states
    
def plot_gunrightsfunding_per_state(top_10_states):
    """plot top 10 states gunrights funding data using matplotlib"""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    N=10
    ind = np.arange(N)                # the x locations for the groups
    width = 0.30                      # the width of the bars
    
    ax2 = ax.twinx()
    gc_2 = [i/1000000 for i in top_10_states['GunControlTotal']]
    gr_2 = [i/1000000 for i in top_10_states['GunRightsTotal']]
    loss_2 = [i/1000 for i in top_10_states['counts']]
    
    
    rects2 = ax.bar(ind+width,gr_2, width,
                    color='blue',
                    error_kw=dict(elinewidth=2,ecolor='blue'),label = "$ in Millions for Gun Rights")
    
    rects4 = ax2.bar(ind+2*width, loss_2, width,
                    color='red',
                    error_kw=dict(elinewidth=2,ecolor='yellow'),label = "No of deaths in 1000s")
    
    # axes and labels
    ax.set_xlim(-width,len(ind)+width)
    ax.set_ylim(0,20)
    ax.set_ylabel('$')
    ax2.set_ylim(0, 5)
    ax2.set_ylabel('People died')
    ax.set_title('$ vs people death')
    xTickMarks = top_10_states['state']
    ax.legend(bbox_to_anchor=(1.6, 1.05))
    ax2.legend(bbox_to_anchor=(1.53, 1.15))
    
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=90, fontsize=10)
    plt.savefig('Plots/grfundingvsdeath.png', dpi=300, bbox_inches='tight')

def plot_funding_per_year(x2,x3,x4,x1):
    """plot funding per year data using matplotlib"""
    N = 5
    gc = [locale.atoi(n[1:]) for n in x2]
    gr = [locale.atoi(n[1:]) for n in x3]
    print(gc,gr)
    g_total = [locale.atoi(n[1:]) for n in x4]
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ind = np.arange(N)                # the x locations for the groups
    width = 0.15                      # the width of the bars
    
    ax2 = ax.twinx()
    gc = [i/1000000 for i in gc]
    gr = [i/1000000 for i in gr]
    loss = [i/10000 for i in x1]
    print(gc,gr,loss)
    rects1 = ax.bar(ind, gc, width,
                color='green',
                error_kw=dict(elinewidth=2,ecolor='red'),label = "$ in Millions for Gun Control")
    
    rects2 = ax.bar(ind+width, gr, width,
                    color='blue',
                    error_kw=dict(elinewidth=2,ecolor='blue'),label = "$ in Millions for Gun Rights")
    
    rects3 = ax2.bar(ind+2*width, loss, width,
                    color='red',
                    error_kw=dict(elinewidth=2,ecolor='yellow'),label = "No of deaths in 10000s")
    
    # axes and labels
    ax.set_xlim(-width,len(ind)+width)
    ax.set_ylim(0,20)
    ax.set_ylabel('$')
    ax2.set_ylim(0, 10)
    ax2.set_ylabel('People died')
    ax.set_title('$ vs people death')
    xTickMarks = ['2014','2015','2016','2017','2018']
    ax.legend(bbox_to_anchor=(1.6, 1.05))
    ax2.legend(bbox_to_anchor=(1.53, 1.15))
    
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=90, fontsize=10)
    plt.savefig('Plots/fundingvsdeathyears_final.png', dpi=300, bbox_inches='tight')
    
def plot_guncontrolfunding_per_state(top_10_states):
    """plot top 10 states gunrights funding data using matplotlib"""
    fig = plt.figure()
    ax = fig.add_subplot(111)
    N=10
    ind = np.arange(N)      
    width = 0.30                    
    
    ax2 = ax.twinx()
    gc_2 = [i/1000000 for i in top_10_states['GunControlTotal']]
    gr_2 = [i/1000000 for i in top_10_states['GunRightsTotal']]
    loss_2 = [i/1000 for i in top_10_states['counts']]
    
    rects1 = ax.bar(ind, gc_2, width,
                color='green',
                error_kw=dict(elinewidth=2,ecolor='red'),label = "$ in Millions for Gun Control")
    
    
    rects4 = ax2.bar(ind+2*width, loss_2, width,
                    color='red',
                    error_kw=dict(elinewidth=2,ecolor='yellow'),label = "No of deaths in 1000s")
    
    # axes and labels
    ax.set_xlim(-width,len(ind)+width)
    ax.set_ylim(0,20)
    ax.set_ylabel('$ in Millions')
    ax2.set_ylim(0, 5)
    ax2.set_ylabel('People died')
    ax.set_title('Gun Control funding vs Gun Violence')
    xTickMarks = top_10_states['state']
    ax.legend(bbox_to_anchor=(1.6, 1.05))
    ax2.legend(bbox_to_anchor=(1.53, 1.15))
    
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=90, fontsize=10)
    plt.savefig('Plots/gcfundingvsdeathperstate.png', dpi=300, bbox_inches='tight')

gun_data_fix()
x1, y1 = create_stack_bar_data('year')
x1 = x1[:-1]
y1 = y1[:-1]
print(x1,y1)
x2,x3,x4 = nra_funding_data()
plot_funding_per_year(x2,x3,x4,x1)
gunDollarsStateDataF = gun_funding_per_state()
top10States = sort_top_10_states(gunDollarsStateDataF)
plot_gunrightsfunding_per_state(top10States)
plot_guncontrolfunding_per_state(top10States)

