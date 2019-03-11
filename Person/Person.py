##region File Information
#
#
#
##endregion
import datetime
from datetime import date

class Person:
    '''Creates Instance of Person'''
    def __init__(self, name, dob): ##todo: set date to yyyymmdd format
        self.__name = name
        self.__dob = dob

    def getName(self):
        return self.__name

    def getDOB(self):
        return self.__dob

    def setName(self, name):
        self.__name = name

    def setDOB(self,dob):
        self.__dob = dob

    def getAge(self):
        today = datetime.datetime.now()
        dobYear = self.__dob[:4]
        dobMonth = self.__dob[4:6]
        dobDay = self.__dob[6:]

        dobDate = datetime.datetime(int(dobYear), int(dobMonth), int(dobDay))
        age = (today-dobDate).days // 365
        return age

    def __str__(self):
        info = "Name: " + self.__name + "\nDoB: " + self.__dob
        return info

def main():
    p1 = Person("A","19971217")
    print(p1)
    print("Age:", p1.getAge())

main()