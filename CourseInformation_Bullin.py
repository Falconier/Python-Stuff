##region Assignment Information
# using dictionaries to organize course information for output
# Jacob Emory Bullin
# 2-15-19
##endregion

def main():
    cRoom, cInstructor, cMeetTime = generateDictionary()
    displayMenu()
    while True:
        command = input("Command:> ").lower().lstrip(" ").rstrip(" ")
        if(command == "list"):
            listAll(cRoom)
        elif(command == "find"):
            findCourse(cRoom,cInstructor,cMeetTime)
        elif(command == "help"):
            displayMenu()
        elif(command == "exit"):
            break
        else:
            print("Invalid command. Please try again\n".upper())
    print("Session ended".title())

def displayMenu():
    print("------Course Information------\n============================== \nlist - list all \nfind - search by course number \nhelp - reprint menu \nexit - exit program \n==============================".title())


def generateDictionary():
    rooms = {"CS101": 3004, "CS102": 4501, "CS103": 6755, "NT110": 1244, "CM241": 1411}
    instructors = {"CS101": "Haynes", "CS102": "Alvarado", "CS103": "Rich", "NT110": "Burke", "CM241": "Lee"}
    meetTime = {"CS101": "8:00 am", "CS102": "9:00 am", "CS103": "10:00 am", "NT110": "11:00am", "CM241": "1:00 pm"}

    return rooms, instructors, meetTime

def listAll(dict):
    j=1
    for key,val in dict.items():
        print(str(j + 1) + ".", key)
        j += 1
    print()

def findCourse(r,i,m):
    num = input("Please Enter A Couse Number: ").upper()
    try:
        print("Course:", num)
        print("Room Number:", r[num])
        print("Instructor:", i[num])
        print("Meeting Time:", m[num])
    except EOFError:
        print("That course does not exist")

main()