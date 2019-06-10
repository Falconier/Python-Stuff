import sys
import os
import sqlite3
from contextlib import closing

from objects import Category
from objects import Movie

conn = None

def connect():
    global conn
    if not conn:
        if sys.platform == "win32":
            DB_FILE = "movies.sqlite"
        else:
            HOME = os.environ["HOME"]
            DB_FILE = HOME + "movies.sqlite"
        
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_category(row):
    return Category(row["categoryID"], row["categoryName"])

def make_movie(row):
    return Movie(row["movieID"], row["name"], row["year"], row["minutes"],
            make_category(row))

def get_categories():
    query = '''SELECT categoryID, name as categoryName
               FROM Category'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories

def get_category(category_id):
    query = '''SELECT categoryID, name AS categoryName
               FROM Category WHERE categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()
        if row:
            return make_category(row)
        else:
            return None

def get_movies_by_category(category_id):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE Movie.categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

def get_movies_by_year(year):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

def add_movie(movie):
    sql = '''INSERT INTO Movie (categoryID, name, year, minutes) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie.category.id, movie.name, movie.year,
                        movie.minutes))
        conn.commit()

def delete_movie(movie_id):
    sql = '''DELETE FROM Movie WHERE movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, str(movie_id))
        test = conn.commit()
        print("Test", test)

def get_movie(movie_id):
    sql = '''SELECT movieID, Movie.name, year, minutes, Movie.categoryID as categoryID, Category.name as categoryName FROM Movie JOIN Category ON Movie.categoryID = Category.categoryID WHERE Movie.movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, str(movie_id))
        result = c.fetchone()
        if result:
            m = make_movie(result)
            return m
        else:
            return None

def get_movies_by_minutes(minutes):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE minutes <= ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (minutes,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies