#%%
from bs4 import BeautifulSoup
html_doc = """
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=iso-8859-1">
        <title>An example of HTML page</title>
    </head>
    <body>
        <h2>This is an example HTML page</h2>
            <p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.
           </p>
           <p>
              <a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from w3resource.com</a>
          </p>
          <p>
          <a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from w3resource.com </a>
          </p>
   </body>
</html>
"""
#%%
#! Write a python program to find the title tags from a given html document.        
soup = BeautifulSoup(html_doc, 'html.parser')

#! Function to read the title tags from a given html document
def find_title():
       
    print(soup.find('title').string)

find_title()
# %%
#! Write a Python program to retrieve all the paragraph tags from a given html document.
simple_soup = BeautifulSoup(html_doc, 'html.parser')
#* Function to read all the paragraphs tags from a given html document
# 
def find_all_paragraphs():     
    
    list_of_ps = simple_soup.find_all('p')
    all_paragraphs = [p for p in list_of_ps]
    return all_paragraphs

lista = find_all_paragraphs()
for p in lista:    
    print(p.text)
# %%
from bs4 import BeautifulSoup

"""
3. Write a Python program to get the number of paragraph tags of a given html document.    
"""

html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>An example of HTML page</title>
</head>
<body>
<h2>This is an example HTML page</h2>
<p>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc at nisi velit,
aliquet iaculis est. Curabitur porttitor nisi vel lacus euismod egestas. In hac
habitasse platea dictumst. In sagittis magna eu odio interdum mollis. Phasellus
sagittis pulvinar facilisis. Donec vel odio volutpat tortor volutpat commodo.
Donec vehicula vulputate sem, vel iaculis urna molestie eget. Sed pellentesque
adipiscing tortor, at condimentum elit elementum sed. Mauris dignissim
elementum nunc, non elementum felis condimentum eu. In in turpis quis erat
imperdiet vulputate. Pellentesque mauris turpis, dignissim sed iaculis eu,
euismod eget ipsum. Vivamus mollis adipiscing viverra. Morbi at sem eget nisl
euismod porta.</p>
<p><a href="https://www.w3resource.com/html/HTML-tutorials.php">Learn HTML from
w3resource.com</a></p>
<p><a href="https://www.w3resource.com/css/CSS-tutorials.php">Learn CSS from 
w3resource.com</a></p>
</body>
</html>
"""
simple_soup = BeautifulSoup(html_doc, 'html.parser')
print("Number of paragraphs tags")
print(len(simple_soup.find_all('p')))
# %%
# 4. Write a Python program to extract the text in the first paragraph tag of 
#   a given html document.

simple_soup = BeautifulSoup(html_doc, 'html.parser')
def find_first_paragraph():     
    
    list_of_ps = simple_soup.find_all('p')
    all_paragraphs = [p.string for p in list_of_ps]
    first_paragraph = all_paragraphs[0]
    return first_paragraph

print(f"The first paragraph found in the given html document is:\n{find_first_paragraph()}")
# %%
