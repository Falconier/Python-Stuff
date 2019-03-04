##region Assignment Information
# AddressBook_v2
# use database for an address book
# Jacob Emory Bullin
# 2-15-19
##endregion

##region Imports
import pyodbc
import pickle
##endregion

##region db connection information
server = 'tcp:jacobemorycfserver.database.windows.net,1433'
database = 'AddressBook'
username = 'Falconier'
password = '9483dae1-8b8e-4959-9919-6b8bab5c035c'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 13 for SQL Server};Server=' + server + ';Database=' + database + ';UID=' + username + ';PWD=' + password)
##endregion

def main():
    bk = dispLoadingMenu()
    adBook = convert(bk)
    displayMenu(adBook)

def dispLoadingMenu():
    # print("Launching Address Book\n1. Load from Database\n2. Load from Backup File")
    # c = input("Enter number to select: ").lstrip().rstrip()
    c='1'
    book = []
    if(c=='1'):
        # attempt load from database
        try:
            cursor = cnxn.cursor()
            cursor.execute('select * from ' + database + '.dbo.EmailBook')
            for row in cursor:
                book.append(row)
            cursor.close()
            del cursor
        # failed load from database, attempt load from backup
        except ConnectionRefusedError:
            print("Failed to load from Database...\nFalling back to Backup File...")
            # attempt load from backup
            try:
                pckl = open("Address_Book_Bullin.data","rb")
                print("Finished loading from backup.")
            # failed load from backup, writing new blank backup
            except(OSError, IOError) as e:
                pckl = open("Address_Book_Bullin.data","wb")
            while(True):
                try:
                    p = pickle.load(pckl)
                    book.append(p)
                except EOFError:
                    break
            pckl.close()
            print("No Backup found, new file initiated")
        return book
    elif(c=='2'):
        # attempt load from backup
        try:
            pckl = open("Address_Book_Bullin.data", "rb")
            print("Finished loading from Backup.")
        # load from backup failed, writing new blank backup
        except(OSError, IOError) as e:
            pckl = open("Address_Book_Bullin.data", "wb")
        while (True):
            try:
                p = pickle.load(pckl)
                book.append(p)
            except EOFError:
                break
        pckl.close()
        print("No Backup found, new file initiated")
    else:
        book = dispLoadingMenu()
    return book

def displayMenu(book):
    print("Address Book\nList - lists address book\nNew - new entry\nUpdate - update entry\nDelete - delete entry\nExit - terminate program")
    while(True):
        com = input("Command:> ").lower().lstrip().rstrip()
        if(com=="list"):
            listBook()
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

def convert(b):
    d = {}
    for e in b:
        tempList = str(e).split(",")
        N = tempList[0].strip("(").strip(")") +" "+ tempList[1].strip("(").strip(")")
        E = tempList[2].strip("(").strip(")")
        d[N] = E

    return d

def listBook():
    b=[]
    try:
        cursor = cnxn.cursor()
        cursor.execute('select * from ' + database + '.dbo.EmailBook')
        for row in cursor:
            b.append(row)
        cursor.close()
        del cursor
    except ConnectionRefusedError:
        print("Failed")
    d = convert(b)
    for e in d:
        print("Name:",e+",","Email:",d[e])
        
        # print(str(e).lstrip('(').rstrip(')').split(",")+)

def new():
    FN = input("enter first name: ")
    LN = input("enter last name: ")
    E = input("enter email address:")
    cursor = cnxn.cursor()
    try:
        cursor.execute("insert into " + database + ".dbo.EmailBook (FirstName, LastName, Email) values (?,?,?)", FN, LN,E)
        cursor.commit()
        print("Entry Added:")
        print(
            cursor.execute("select * from " + database + ".dbo.EmailBook where FirstName = (?) and LastName = (?)", FN,
                           LN))
        cursor.close()
        del cursor
    except IOError:
        print("Failed to make new entry")

def update(b):
    listBook(b)
    FN = input("enter first name: ")
    LN = input("enter last name: ")
    E = input("enter email address:")
    cursor = cnxn.cursor()
    try:
        cursor.execute("update "+database+".dbo.EmailBook set Email = (?) where FirstName = (?) and LastName = (?)", E,FN,LN)
        cursor.commit()
        print("Updated Entry:")
        print(cursor.execute("select * from "+database+".dbo.EmailBook where FirstName = (?) and LastName = (?)",FN,LN))
        cursor.close()
        del cursor
    except IOError:
        print("Entry does not exist with the name "+FN, LN)

def delete(b):
    FN = input("enter first name: ")
    LN = input("enter last name: ")
    cursor = cnxn.cursor()
    try:
        cursor.execute("delete from "+database+".dbo.EmailBook where FirstName = (?) and LastName = (?)",FN,LN)
        cursor.commit()
        cursor.close()
        del cursor
    except IOError:
        print("Deletion failed. No entry exist with the name "+FN,LN)


main()