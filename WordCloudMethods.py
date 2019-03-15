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

import io
from collections import Counter
from os import path
from wordcloud import WordCloud # for plotting the wordle like plot (wordcloud)
import re, string # for regular expression matching

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
%matplotlib inline


def incident_characteristics(pd_gun, column_name = 'incident_characteristics'):
    '''
    Returns a dictionary with a frequency count of the incident charactieristics
    Input:
        pd_gun: dataframe with incident characteristics column
    Output:
        characterisation_words_dict: Dictionary as mentioned above
    '''
    assert isinstance(pd_gun,pd.DataFrame)
    assert isinstance(column_name,str)
    characterisation_words_dict = defaultdict(int)
    for i in range(pd_gun.shape[0]):
        for j in re.split('\|| |; |, |\*|\n',str(pd_gun.loc[i]['incident_characteristics']).translate(None, string.punctuation) ):
            characterisation_words_dict[j]+=1
    return characterisation_words_dict
    

def word_cloud(filename = 'desc_words.txt', font_path = 'Symbola.ttf'):
    '''
    Generate wordcloud of the words given and save the plot
    Input:
        filename with the words in it
    Output:
        matplotlib object
    '''
    assert isinstance(filename,str)
    assert isinstance(font_path,str)
    
    text = io.open(filename).read()
    words = text.split()
    word_cloud = WordCloud(font_path=font_path).generate(text)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.savefig('wordle.png',dpi=300)
    return plt