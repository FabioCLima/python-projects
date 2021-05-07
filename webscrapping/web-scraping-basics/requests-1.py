# Request api 
#
#%%
#! Bibliotecas 
import requests 
import json
import webbrowser 

from pprint import pprint

print(requests.__version__)
# %%
resp = requests.get('https://jsonplaceholder.typicode.com/todos/1')
type(resp)
# %%
resp.status_code #! status code property gives you the status of the response
# %%
type(resp.headers)
# %%
pprint(resp.headers)
# %%
data = resp.text #! contents of the response are returned in the json format
print(data) #! json format
# %%
#! Json format parse into python format
data = json.loads(resp.text) #! json.loads convert to dicionary python 
pprint(data)
# %%
wikipedia_search_url = 'https://en.Wikipedia.org/wiki/Special:Search'
webbrowser.open(wikipedia_search_url)
# %%
query_params = {'search' : 'requests'}

resp = requests.get(url = wikipedia_search_url, 
                    params= query_params)
# %%
resp
# %%
resp.url
# %%
webbrowser.open('https://en.wikipedia.org/wiki/Requests')
# %%
#! Post Json data send to the server requests
post_data = {
    'title'  : 'some_title',
    'body'   : 'some_body',
    'userId' : 22
}

resp = requests.post('https://jsonplaceholder.typicode.com/posts', data = post_data)
# %%
resp
# %%
json.loads(resp.text)
# %%
resp = requests.get('https://httpbin.org/absolute-redirect/5')
# %%
pprint(resp.history)
# %%
resp.status_code
# %%
resp.url
# %%
def print_response_history(resp):     
    
    if resp.history:     
        print("History")
        for r in resp.history:    
            print(r.status_code, r.url)
            
        print("Finally")
        print(resp.status_code, r.url)
        
    else:     
        print("Request was not redirected")
# %%
print_response_history(resp)
# %%
resp = requests.get('https://www.google.com/redirect-to?url=https://yahoo.com')
print_response_history(resp)
# %%
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

resp = requests.get(url, timeout = 2)
# %%
resp
# %%
data = resp.json()
print(data)
# %%
type(data)
# %%
data[0]['title']
import pandas as pd 
# %%
issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
issues
# %%
