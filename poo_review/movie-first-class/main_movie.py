from first_class import Movie


my_movie = Movie('Lord of the Rings', 'Peter Jackson')
print(f"O objeto instanciado my_movie é do tipo: \n{my_movie} e está no \
      endereço de memória mostrado.")
print("\n")
print(my_movie.name)
my_movie.print_info()
