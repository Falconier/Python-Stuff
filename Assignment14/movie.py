##region File information
# Jacob Emory Bullin
# movie.py
# movie object class
##endregion

import sqlite3

class Movie():
    def __init__(self, movieId, catId, name, year, runTime):
        self.Id = movieId
        self.categoryId = catId
        self.Title = name
        self.year = year
        self.minutes = runTime

        