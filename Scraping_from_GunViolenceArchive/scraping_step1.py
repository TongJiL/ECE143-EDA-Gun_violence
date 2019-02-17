import urllib2
import bs4
from urllib2 import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict
from bs4.element import Comment

def tag_visible(element):
	'''
	Remove unnecessary tags from html
	Input:
		element of the HTML
	Output:
		Boolean (to include or exclude the element)
	'''
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_list_from_html(body):
	'''
	Function to filter out the non-text elements
	First it parses using the beautifulsoup module
	Input:
		body of the raw html
	Output
		list of visible texts
	'''
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return [x.strip().rstrip('<').lstrip('>') for x in visible_texts if (x != '\n') and (x != '>\n')]

#######
# Read the avaialble URLs from Kaggle
#######
df = pd.read_csv('gun-violence-data_01-2013_03-2018.csv')
urls = df['incident_url'].tolist()


######
# Scraping from the URLs
######
incident_id = 0
data_list=[]
for url in urls[0:20]:
    incident_id+=1
    data_dict={}
    data_dict['incident_id']=incident_id
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib2.urlopen( req )
    html=str(con.read())
    soup_in=html.split('block-system-main')[1:]
    num_of_subheaders = len(soup_in[0].split("h2"))
    elements = soup_in[0].split("h2")
    loc =  [x for x in text_list_from_html(elements[2]) if any(s in x for s in list_of_states)][0].split(',')
    data_dict['city/county']=''.join(loc[0:-1])
    data_dict['state']=loc[-1]
    data_list.append(data_dict)
    for i in range(1,num_of_subheaders ):
        if i==num_of_subheaders-1:
            pass
            #print text_list_from_html(elements[i].split("/div")[0])
        else:
            pass
            #print text_list_from_html(elements[i])
    