#%%
class Garage:    
    
    def __init__(self) -> None:
        self.cars = []
    
    #! dunder method that give us the size of the list object    
    def __len__(self):    
        return len(self.cars)
    #! dunder method that allows us get an item of list
    def __getitem__(self, i):    
        return self.cars[i]
    
    #! dunder method to printout the string that represents the object
    #! useful information for the devoloper
    #! useful in debug step: code oriented description
    def __repr__(self) -> str:
        return f'<Garage {self.cars}>'
    
    #! dunder method to represents to the user the object 
    #! code oriented to user description 
    def __str__(self) -> str:
        return f'Garage with {len(self)} cars.'
        
# %%
ford = Garage()   #* instanciando o objeto ford que é uma lista por definição
ford.cars.append("Fiesta")
ford.cars.append('Focus')
print(ford.cars)
print(f'How many cars are in the garage ford ?\nThere are {len(ford)} \
      cars in the garage ford')
# %%
print(ford[0]) #! Garage.__getitem__(ford, 0)
# %%
for car in ford:    
    print(car)
# %%
print(ford)
# %%
