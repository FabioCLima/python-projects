# Import packages
#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd 

#! Download and parse the HTML
start_url = 'https://en.wikipedia.org/wiki/Tesla,_Inc.'

#! Download the HTML from start_url
downloaded_html = requests.get(start_url)

#! Parse the HTML with BeautifulSoup and create a soup object
soup = BeautifulSoup(downloaded_html.text)

#! Save a local copy
with open("downloaded.html", "w") as file:     
    #* Depending on the HTML page, on the next line, you may have to use 
    #* soup.prettify().encode('UTF-8')
    
    file.write(soup.prettify())
    
#%%