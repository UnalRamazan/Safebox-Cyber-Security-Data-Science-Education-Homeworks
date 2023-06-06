class Movie:
    def __init__(self, title, year, director):
        self.title = title
        self.year = year
        self.director = director

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "director": self.director
        }

    @classmethod
    def from_dict(cls, movie_dict):
        return cls(
            title=movie_dict["title"],
            year=movie_dict["year"],
            director=movie_dict["director"]
        )
