#%% 
# importing the module
import wikipedia

# %%
page = wikipedia.page("beach")
# %%
type(page)
# %%
dir(page)
# %%
page.summary
# %%
page.images
# %%
len(page.images)
# %%
page.images[0]
# %%
import requests
# %%
link = page.images[0]
# %%
headers ={'User-agent': 'Mozilla/5.0'}
req = requests.get(link, headers= headers)
with open("beach.jpg", 'wb') as file:
    file.write(req.content)
# %%
