from FilmDepot import FilmDepot
from Movie import Movie


class MovieSystem:
    def __init__(self, file_name):
        self.film_depot = FilmDepot(file_name)

    def add_movie(self):
        title = input("Enter the title of the movie: ")
        year = int(input("Enter the year of release: "))
        director = input("Enter the director's name: ")
        new_movie = Movie(title, year, director)
        self.film_depot.add_movie(new_movie)

    def delete_movie(self):
        title = input("Enter the title of the movie to delete: ")
        self.film_depot.delete_movie(title)

    def search_movie(self):
        title = input("Enter the title of the movie to search: ")
        self.film_depot.search_movie(title)

    def show_all_movies(self):
        self.film_depot.get_all_movies()

    def display_menu(self):
        menu = """
        Movie System Menu:
        1. Add a movie
        2. Delete a movie
        3. Search for a movie
        4. Show all movies
        5. Quit

        Enter your choice (1-5): 
        """
        while True:
            choice = input(menu)
            if choice == '1':
                self.add_movie()
            elif choice == '2':
                self.delete_movie()
            elif choice == '3':
                self.search_movie()
            elif choice == '4':
                self.show_all_movies()
            elif choice == '5':
                print("Exiting Movie System...")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
