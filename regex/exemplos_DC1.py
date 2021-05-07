#%%
import re          

text = "Date of start: 4-3. Date of registration: 10-04."
re.findall(r"\d+-\d+", text)
# %%
#! Quantifiers
#* Zero times or more: *
my_string = "The concert was amazing! @ameli!a @joh&&n @mary90"

re.findall(r"@\w+\W*\w+", my_string)
# %%
#! ? zero times or once 
text = "The color or this image is amazing. However, the colour blue could be brighter."

regex = r"colou?r"
re.findall(regex, text)
# %%
#* [a-z,A-Z and 0-9] : a between z - lower case, A between Z uppercase
#* qq digito entre zero e nove
'''Write a Python program to check that a string contains only a certain set 
of characters (in this case a-z, A-Z and 0-9). '''

import re          
def is_allowed_specific_char(string):     
    
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))
# %%
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# %%
string = "4506 people attend the show"
print(re.search(r"\d{4}", string))
# %%
print(re.match(r"\d{4}", string))
# %%
re.search(r"\d+", "Yesterday, I saw 3 shows")
# %%
print(re.match(r"\d+", "Yesterday, I saw 3 shows"))
# %%
txt = "The rain in Spain"
x = re.search(r"\^[ai]", txt)
print(x)
# %%
my_links = "Just check out this link: www.amazingpics.com. It has amazing photos!"
x = re.findall(r"w{3}.+com", my_links)
print(x)
# %%
my_strings = "the 80s music was much better that the 90s"
x = re.findall(r"^the\s\d+s", my_strings)
print(x)
# %%
x = re.findall(r"the\s\d+s$", my_strings)
print(x)
# %%
my_string = "I love the music of Mr.Go. However, the sound was too loud."
x = re.split(r"\.\s", my_string)
print(x)
# %%
my_string = "Elephants are the world's largest land animal!, I would love to see an elephant one day."
x = re.findall(r"Ele\w+|ele\w+", my_string)
print(x)
# %%
my_string = 'Yesterday I spent my afternoon with my friends: MaryJohn2 Clary3'
x = re.findall(r"[a-zA-Z]+\d", my_string)
print(x)
# %%
x = re.findall(r"[A-Za-z]+\d", my_string)
print(x)
# %%
my_string = "My&name&is#John Smith. I%live$in#London."
x = re.sub(r"[#$%&]", " ", my_string)
print(x)
# %%
my_links = "Bad website: www.99.com. Favorite site: www.hola.com"
x = re.findall(r"www[^0-9]+com", my_links)
print(x)
# %%
