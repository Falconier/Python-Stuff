# manage movie collections
# By: Jacob Emory Bullin
# 2-13-19

##region stuff needed
# list - list all
# add - add movie
# del - delete movie
# find - search by year
# exit - exit program
# movie (class) - name, year, rating
##endregion

import pickle

def main():
    displayMenu()
    movies = loadCollection()
    while True:
        command = input("Command:> ").lower().lstrip(" ").rstrip(" ")
        # command = command.lower()
        if(command == "list"):
            listAll(movies)
        elif(command == "add"):
            addMovie(movies)
        elif(command == "del"):
            delMovie(movies)
        elif(command == "find"):
            findMovie(movies)
        elif(command == "migrate"):
            migrate(movies)
        elif(command == "reload"):
            movies.clear()
            movies = loadCollection()
            print("RELOADED COLLECTIONS\n")
        elif(command == "exit"):
            break
        else:
            print("Invalid command. Please try again\n".upper())
    print("Session ended".title())

## loads the collection from a file
def loadCollection():
    print("Loading Files")
    try:
        pckl = open("Movie Collection.data","rb")
    except(OSError, IOError) as e:
        pckl = open("Movie Collection.data","wb")
    m = []
    while (True):
        try:
            p = pickle.load(pckl)
            m.append(p)
        except EOFError:
            # print("no information left \n" + info)
            break
    pckl.close()
    print("Finished Loading Files \n")
    return m

def displayMenu():
    print("----Movie Collection----\n======================== \nlist - list all \nadd - add movie \ndel - delete movie \nfind - search by year \nmigrate - updates/saves file \nreload - reload file \nexit - exit program \n========================".title())

def listAll(movieList):
    if(len(movieList) == 0):
        print("no movies in list. please add some".title())
        return
    else:
        try:
            i = 0
            for movie in movieList:
                row = movie
                print(str(i+1) + ".", row[0], "(" + row[1] + ")", "\"" + row[2] + "\"")
                i += 1
            print()
        except ValueError:
            print("list is null")

def addMovie(movieList):
    name = input("Name of movie: ").title().rstrip(" ").lstrip(" ")
    year = input("Year of release: ")
    rating = input("Rating (G, PG, PG-13, R, NC-17): ").upper().rstrip(" ").lstrip(" ")
    movie = []
    movie.append(name)
    movie.append(year)
    movie.append(rating)
    movieList.append(movie)
    print("\"" + movie[0] + "\"", "was added to the colleciton")

def delMovie(movieList):
    name = input("Name of movie to delete: ").title()
    delSome = False
    for movie in movieList:
        if(movie[0] == name):
            try:
                yOn = input("Are you sure you want to delete this movie? (y/n):> ").upper()
                if(yOn == "Y"):
                    movieList.remove(movie)
                    delSome = True
                    print("\"" + name + "\"", "was removed")
                else:
                    print("\"" + name + "\"", "was not removed")
                    break
            except LookupError:
                print("Index does not exist")
    if not delSome:
        print("\"" + name + "\"", "does not exist")

def findMovie(movieList):
    year = input("enter the year that you are looking for: ").lstrip().rstrip()
    yearMovies = []
    i = 0
    for movie in movieList:
        if(movie[1] == year):
            yearMovies.append(movie)
        else:
            continue
    for m in yearMovies:
        row = m
        print(str(i + 1) + ".", row[0], "(" + row[1] + ")", "\"" + row[2] + "\"")
        i += 1
    print()

## updates/saves the editable list to the file
def migrate(movieList):
    yOn = input("ARE YOU SURE THAT YOU WANT TO MIGRATE INFORMAITON?\nThis will overwrite any data that currently exists!\n(y/n) :>> ").upper()
    if(yOn == "Y"):
        pckl = open("Movie Collection.data","ab")
        try:
            pckl.truncate(0)
        except EOFError:
            print("Migration Failed: Overwriting Failure")

        pckl.writable()
        for m in movieList:
            try:
                pickle.dump(m,pckl)
            except EOFError:
                print("Migration Failed: Dump Failure")
                break
        pckl.close()
    else:
        return

if __name__ == "__main__":
    main()