class Movie:

    def __init__(self, movie_name, movie_director):
        """[A movie class with name and director as properties]

        Args:
            movie_name ([string]): [Movie's name]
            movie_director ([string]): [Movie's director]
        """
        self.name = movie_name
        self.director = movie_director

    def __str__(self) -> str:
        """[representation of the object for development purposes]
        Returns:
            str: [Movie object description - name and director properties]
        """
        return f"<Movie: {self.name} by {self.director}>"

    def print_info(self):
        """[method that prints out the movie's information]
        """
        print(f'<<{self.name}>> by {self.director}')
