# %%
try:
   a = int(input("Please enter a number: "))
   print(f'{a} squared is {a*a}')
except:
   print("Wrong input type! You must enter a number!")
# %%
try:
   dict_a = {1:'Max', 2:'Ashley', 3:'John'}
   number = int(input(f'Pick a number from the list:{list(dict_a.keys())}'))
   print(dict_a[number])
except KeyError:
   print(f'{number} is not in the list')
except ValueError:
   print('You must enter a number!')
# %%
