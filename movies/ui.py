#!/usr/bin/env/python3

import db
from objects import Movie

def display_title():
    print("The Movie List program")
    print()    
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("min - gets movies with equal to or less than time specified.")
    print("exit - Exit program")
    print()    

def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()    
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()

def display_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        print(line_format.format(str(movie.id), movie.name,
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()    

def display_movies_by_category():
    category_id = int(input("Category ID: "))
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())
    
def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))

def add_movie():
    name        = input("Name: ")
    year        = int(input("Year: "))
    minutes     = int(input("Minutes: "))
    category_id = int(input("Category ID: "))
    
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:        
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_movie(movie)    
        print(name + " was added to database.\n")

def delete_movie():
    movie_id = int(input("Movie ID: "))
    m = get_movie(movie_id)
    mID = m.getID()
    dell = input("Are you sure that you want to delete " + m.getName()+ " ? (Y/N) ")
    if(dell.capitalize().rstrip(' ').lstrip(' ') == "Y"):
        db.delete_movie(movie_id)
        print("Movie ID " + str(movie_id) + " was deleted from database.\n")
    else:
        print("Operation Canceled")

def get_movie(movie_id):
    # movie_id = int(input("Movie ID: "))
    m = db.get_movie(movie_id)
    return m

def display_movies_by_minutes():
    minutes = int(input("How quick of a movie would you like in minutes?  "))
    print()
    movies = db.get_movies_by_minutes(minutes)
    display_movies(movies, str(minutes))


        
def main():
    db.connect()
    display_title()
    # display_categories()
    while True:        
        command = input("Command: ")
        if command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "exit":
            break
        elif command == "get":
            get_movie()
        elif command == 'min':
            display_movies_by_minutes()

        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
