import urllib2
import bs4
from urllib2 import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict
from bs4.element import Comment


def text_list_from_html(body):
	'''
	Function to filter out the non-text elements
	First it parses using the beautifulsoup module
	Input:
		body of the raw html
	Output
		list of visible texts
	'''
    assert isinstance(body,str)
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return [x.strip().rstrip('<').lstrip('>') for x in visible_texts if (x != '\n') and (x != '>\n')]

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

if __name__ == '__main__':

    '''
    # Read the avaialble URLs from Kaggle
    '''
    df = pd.read_csv('gun-violence-data_01-2013_03-2018.csv')
    urls = df['incident_url'].tolist()
    list_of_states = df['state'].unique().tolist()

    '''
    # Scraping from the URLs
    '''

    incident_id = 0
    data_list=[]
    for url in urls:
        incident_id+=1
        data_dict={}
        data_dict['incident_id']=incident_id
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
        con = urllib2.urlopen( req )
        html=str(con.read())
        soup_in=html.split('block-system-main')[1:]
        num_of_subheaders = len(soup_in[0].split("h2"))
        elements = soup_in[0].split("h2")
        data_dict['n_killed']=''.join(text_list_from_html(elements[4])).count("Killed") # Num of killed
        data_dict['n_injured'] = ''.join(text_list_from_html(elements[4])).count("Injured") # Num of injured
        loc =  [x for x in text_list_from_html(elements[2]) if any(s in x for s in list_of_states)][0].split(',')
        data_dict['city/county']=''.join(loc[0:-1]) # City/County
        data_dict['state']=loc[-1] # State
        data_dict['date'] = text_list_from_html(elements[2])[0] # Date
        [lati,longi] =  text_list_from_html(elements[2])[-2][13:].split(',') # Latitude and Longitude
        data_dict['latitude'] = lati
        data_dict['longitude'] = longi
        data_list.append(data_dict)

        
        