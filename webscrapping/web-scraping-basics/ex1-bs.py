import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.plugshare.com')
soup =  BeautifulSoup(resp.text, 'html.parser')
print(soup.prettify)