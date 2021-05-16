
{
    'name'       : 'The Matrix',
    'director'   : 'Wachowshi'
}

#* my_movie = MOVIE('The Matrix', 'Wachowski')
#%%
#! Define a Movie class that has two properties: name of the movie and the director
class Movie:
    
    def __init__(self, movie_name, movie_director):
        """[summary]

        Args:
            movie_name ([string]): [Movie's name]
            movie_director ([string]): [Movie's director]
        """        
        self.name = movie_name
        self.director = movie_director
    
    def __str__(self) -> str:
        """[representação em string descrevendo o objeto]
        Returns:
            str: [objeto do tipo Movie com atributos name e director]
        """        
        return f"<Movie: {self.name} by {self.director}>"
    
    def print_info(self):
        """[método da classe usado para informar sobre o objeto]
        """        
        print(f'<<{self.name}>> by {self.director}')


my_movie = Movie('Lord of the Rings', 'Peter Jackson')
print(f"O objeto instanciado my_movie é do tipo: \n{my_movie} e está no endereço de memória mostrado.")
print("\n")
print(my_movie.name)
my_movie.print_info()