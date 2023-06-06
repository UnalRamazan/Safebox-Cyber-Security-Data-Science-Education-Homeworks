import json
from Movie import Movie


class FilmDepot:
    def __init__(self, file_name):
        self.file_name = file_name
        self.movies = self.load_movies_from_file()

    def load_movies_from_file(self):
        try:
            with open(self.file_name, 'r') as file:
                movies_list = json.load(file)
                return [Movie.from_dict(movie) for movie in movies_list]
        except FileNotFoundError:
            return []

    def write_movies_to_file(self):
        movies_list = [movie.to_dict() for movie in self.movies]
        with open(self.file_name, 'w') as file:
            json.dump(movies_list, file, indent=4)

    def add_movie(self, movie):
        self.movies.append(movie)
        self.write_movies_to_file()
        print("Movie added successfully.")

    def delete_movie(self, movie_title):
        for movie in self.movies:
            if movie.title == movie_title:
                self.movies.remove(movie)
                self.write_movies_to_file()
                print("Movie deleted successfully.")
                return
        print("Movie not found.")

    def search_movie(self, movie_title):
        found_movies = []
        for movie in self.movies:
            if movie.title.lower() == movie_title.lower():
                found_movies.append(movie)
        if found_movies:
            print("Search Results:")
            for movie in found_movies:
                print(movie.to_dict())
        else:
            print("Movie not found.")

    def get_all_movies(self):
        if self.movies:
            print("All Movies:")
            for movie in self.movies:
                print(movie.to_dict())
        else:
            print("No movies found.")
