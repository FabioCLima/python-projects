#%%
#? Libraries need to work in this scrapping script
import requests
from bs4 import BeautifulSoup

#! requests.get = getting the html content
page = requests.get('http://www.example.com')
page  # <Response [200]> indica ok o servidor respondeu
# %%
print(page.content)
# %%
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.text)
# %%
locator_h1 = soup.find('h1').string #localizando o header1
print(locator_h1)
# %%
locator_paragraph = soup.find('p').string
print(locator_paragraph)
# %%
locator_href = soup.select_one('div p a')
item_link = locator_href.attrs['href']
print(item_link)
# %%
