#%% 
import re  
from bs4 import BeautifulSoup 


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
                <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''
#?:criando o objeto beautifulsoup e instanciando-o com o html documento de 
#? análise

soup = BeautifulSoup(ITEM_HTML, 'html.parser')

#! Find the title book - find item name
def find_item_name():   
    
    locator = 'article.product_pod h3 a' #! CSS locator - parent.class of parent children children
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['title'] #! access the attribute of the link - title name of the book
    print(item_name)

find_item_name()   
# %%
#! Find the link page
def find_item_page_link():      
    locator = 'article.product_pod h3 a'
    item_url = soup.select_one(locator).attrs['href'] 
    return item_url


find_item_page_link()
# %%
#! Find the books price
def find_item_price():   
    locator = 'article.product_pod  div.product_price p.price_color'
    item_price = soup.select_one(locator).string
    pattern = r"£([0-9]{2}\.[0-9]{2})"   #@ minha solução
    pattern2 = r"£([0-9]+\.[0-9]+)"      #! solução do professor
    matcher = re.findall(pattern, item_price)#@ minha solução
    matcher2 = re.search(pattern, item_price) #teacher's solution
    print(float(matcher[0]))
    print(matcher2.group(0))        #@
    print(float(matcher2.group(1))) #@

find_item_price()
# %%
#! Find the item rating
def find_item_rating():   
    locator = 'article.product_pod p.star-rating'
    star_rating_element = soup.select_one(locator)
    classes = star_rating_element.attrs['class']
    
    #! list compreension 
    # rating_classes = [r for r in classes if r != 'star -rating']
    #! rating_classes = filter(function, iteravel = lista(classes))
    
    rating_classes = list(filter(lambda x: x != 'star-rating', classes))
    #* print(f"The book on the page has rating of {rating_classes[0]}")
    print(rating_classes[0])

find_item_rating()
# %%
#! You can then turn it into a dictionary or whichever
#! way is easiest to store and work with:

item = {
    'name': find_item_name(),
    'link': find_item_page_link(),
    'price': find_item_price(),
    'rating': find_item_rating()
}

print(item)

#! Of course you could make a class which stores this data and
#! has methods to extract it, more on the 'class_html_parsing.py file!
