#* Entendendo o beautifulsoup
#******************************************************************************
#%%
from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

#! Criando o objeto do beautifulsoup - *_soup
simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

#! Função para ler o título do html
def find_title():
    h1_tag = simple_soup.find('h1')    
    print(h1_tag.string)

find_title()

#! Função para printar o conteúdo que está na lista <li>
def find_list_items():      
   list_items = simple_soup.find_all('li')
   list_content = [e.string for e in list_items]
   print(list_content)
   
find_list_items()

#! Função para printar o conteúdo do paragráfo
def find_paragraph():    
    print(simple_soup.find('p', {'class':'subtitle'}).string)
    
find_paragraph()

#! Função para printar o conteúdo do último paragráfo
paragraphs = simple_soup.find_all('p')
#! colocando uma lista vazia dentro da checagem do class para evitar que retorne NONE
#! no caso de não achar class, o que tornaria a sentença não iterável
other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
print(other_paragraph[0].string)
# %%
