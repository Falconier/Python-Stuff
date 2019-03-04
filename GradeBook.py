##region GradeBook.py
# create a gradebook and store it in binary format
# Retrieve and print the gradebook
# By Jacob Emory Bullin
# 2-6-19
##endregion

import pickle

def main():
    gradeBook = createGradeBook()
    printGrades(gradeBook)

def createGradeBook():
    pckl_on = open("CSC121.data","wb")
    pickle.dump("Amy, 100, 95, 98", pckl_on)
    pickle.dump("Brad, 85, 90, 100", pckl_on)
    pckl_on.close()

    return "CSC121.data"

def printGrades(fileName):
    pckl_off = open(fileName, 'rb')
    grades = ""
    while(True):
        try:
            grades += pickle.load(pckl_off)
            grades += "\n"
        except EOFError:
            print("Grades: \n" + grades)
            break

    pckl_off.close()

main()