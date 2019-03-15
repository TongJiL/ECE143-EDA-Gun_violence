import seaborn as sns
import pandas as pd # package for high-performance, easy-to-use data structures and data analysis
import numpy as np # fundamental package for scientific computing with Python
import matplotlib
import matplotlib.pyplot as plt # for plotting
import seaborn as sns # for making plots with seaborn
color = sns.color_palette()
from plotly.offline import init_notebook_mode, iplot # for interactive plotting
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.offline as offline
offline.init_notebook_mode()
from plotly import tools
import plotly.tools as tls
from numpy import array
from matplotlib import cm
from collections import defaultdict  # default dictionary

import folium # For interactive map

import io
from collections import Counter
from os import path
from wordcloud import WordCloud # for plotting the wordle like plot (wordcloud)


# import cufflinks and offline mode
import cufflinks as cf
cf.go_offline()

from sklearn import preprocessing
# Supress unnecessary warnings so that presentation looks clean
import warnings
warnings.filterwarnings("ignore")

# Print all rows and columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


us_state_abbrev = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
    'DC': 'Washington, DC'
}


top_states_mental_health = ['New Hampshire',
 'Wisconsin',
 'Illinois',
 'Pennsylvania',
 'Oregon',
 'New Jersey',
 'Tennessee',
 'California',
 'Utah',
 'Nebraska',
 'Washington',
 'Connecticut',
 'Kentucky',
 'Minnesota',
 'Ohio',
 'Michigan',
 'North Carolina',
 'Alabama',
 'Georgia',
 'Indiana']


#######
# Read Datasets
#######


#mh_14 = pd.read_csv('MH14.csv')
#mh_16 = pd.read_csv('MH16.csv')
#mh_17 = pd.read_csv('MH17.csv')
#mh_18 = pd.read_csv('MH18.csv')


#######
#
#######


def mental_illness_indicator(df, col_state, col_family_hist):
    '''
    Indicator for mental illness history for a particular year
    Input:
        df: dataframe of particular year
        col_state: column name for the state in the dataframe
        col_family_hist: column name for the mental illness history in the dataframe
    Output:
        df_2: dataframe with indicator yes/no for mental illness history 

    '''
    assert isinstance(col_state,str)
    assert isinstance(col_family_hist,str)
    assert isinstance(df,pd.DataFrame)

    df_1 = df.groupby([col_state,col_family_hist])[col_family_hist].count()
    df_2 = df_1.unstack(level=-1)
    df_2['No_']=df_2['No']*100./(df_2['No']+df_2['Yes'])
    df_2['Yes_']=df_2['Yes']*100./(df_2['No']+df_2['Yes'])
    df_2 = df_2.sort_values(by=['Yes_'],ascending=False)
    return df_2


def rename_columns(df,year):
    '''
    renames columns to match all dataframes
    Input:
        df: dataframe
        year: year of the data
    Output:
        x1: renamed dataframe
    
    '''
    assert isinstance(df,pd.DataFrame)
    assert isinstance(year, int)
    i=0
    if year==2014:
        i=1
    elif year==2016:
        i=2
    elif year==2017:
        i=3
    elif year==2018:
        i=4
    x1 = df[['Yes','No']].reset_index()
    if year==2014:
        x1['state']=x1['state'].apply(lambda x: us_state_abbrev[x])
    x1.rename(columns={'state': 'state', 'Yes': 'yes_'+str(i),'No': 'no_'+str(i)}, inplace=True)
    return x1


def combine_all_years(x1,x2,x3,x4):
    '''
    Combine all years data
    Input:
        x1,x2,x3,x4
    Output:
        final_df: final merged dataframe
    '''
    assert isinstance(x1,pd.DataFrame)
    assert isinstance(x2,pd.DataFrame)
    assert isinstance(x3,pd.DataFrame)
    assert isinstance(x4,pd.DataFrame)
    
    m1 = pd.merge(x1,x2, on ='state', how='outer')
    m2 = pd.merge(m1,x3, on ='state', how='outer')
    m3 = pd.merge(m2,x4, on ='state', how='outer')
    m3.fillna(0, inplace=True)
    m3['YES']=m3['yes_1']+m3['yes_2']+m3['yes_3']+m3['yes_4']
    m3['NO']=m3['no_1']+m3['no_2']+m3['no_3']+m3['no_4']
    m3['No_percent']=m3['NO']*100./(m3['NO']+m3['YES'])
    m3['Yes_percent']=m3['YES']*100./(m3['NO']+m3['YES'])
    m3.set_index('state')
    final_df = m3[m3['state'].isin(top_states_mental_health)]
    return final_df
    





