##region Assignment Information
# AddressBook_v1
# use file for an address book
# Jacob Emory Bullin
# 2-15-19
##endregion

##region Imports
import pickle
##endregion

def main():
    book = loadBook()
    displayMenu(book)


def displayMenu(book):
    print("Address Book\nList - lists address book\nNew - new entry\nUpdate - update entry\nDelete - delete entry\nExit - terminate program")
    while(True):
        com = input("Command:> ").lower().lstrip().rstrip()
        if(com=="list"):
            listBook(book)
        elif(com=="new"):
            new()
        elif(com=="update"):
            update(book)
        elif(com=="delete"):
            delete(book)
        elif(com=="exit"):
            break
        else:
            print("Invalid command. Please try again\n".upper())
    print("Session Ended")

def loadCollection():
    print("Loading Files")
    try:
        pckl = open("Movie Collection.data","rb")
    except(OSError, IOError) as e:
        pckl = open("Movie Collection.data","wb")
    b = []
    while (True):
        try:
            p = pickle.load(pckl)
            b.append(p)
        except EOFError:
            # print("no information left \n" + info)
            break
    pckl.close()
    print("Finished Loading Files \n")
    return b

def convert(b):
    d = {}
    for e in b:
        tempList = str(e).split(",")
        N = tempList[0].strip("(").strip(")") + " " + tempList[1].strip("(").strip(")")
        E = tempList[2].strip("(").strip(")")
        d[N] = E