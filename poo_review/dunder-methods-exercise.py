# Exercise: magic methods in Python
# 
#%%
class Club:   
    def __init__(self, name) -> None:
        self.name = name 
        self.players =[]
        
    def __len__(self):      
        return len(self.players)
    
    #* define a method that allows us to access the i-th player in the club directly via indexing.
    #* for example, if some_club is an object of Club class,
    #* we can access the i-th player in some_club like this (you may assume i is always valid):
    #* some_club[i]
    def __getitem__(self, i):      
        return self.players[i]
    
    #* define a method that returns a string representation of this object,
    #* which can be used to recreate this object.
    #* The return value should be in such format (beware of the spacing):
    #* Club {club_name}: {list_of_players}
    #* the club_name and list_of_players should be replaced by the according value of current object
    def __repr__(self) -> str:
        return f'Club {self.name}: {self.players}'
    
    
    #* define a method that returns a readable string representation of this object for the user.
    #* The return value should be in such format (beware of the spacing):
    #* Club {club_name} with {count_of_players} players
    #* the club_name and count_of_players should be replaced by the according value of current object
    def __str__(self) -> str:
        return f'Club {self.name} with {len(self)} players'
    
# %%
flamengo = Club('Flamengo')
flamengo.players.append('Gabi Gol')
flamengo.players.append('Everton Ribeiro')
flamengo.players.append('Diego Alves')
# %%
print(flamengo.__str__)
# %%
