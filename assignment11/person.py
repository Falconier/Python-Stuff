#region File Information
# person.py
# Jacob Emory Bullin
##endregion

class Person:

    def __init__(self, name, address, age, phoneNum):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phNum = phoneNum

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getAge(self):
        return self.__age

    def getPhone(self):
        return self.__phNum

    def setName(self,name):
        self.__name = name

    def setAddress(self, address):
        self.__address = address

    def setAge(self, age):
        self.__age = age

    def setPhone(self, phoneNum):
        self.__phNum = phoneNum

    def __str__(self):
        info = ""
        info += "Name: " + self.getName() + " Address: " + self.getAddress() + " Age: " + str(self.__age) + " Phone: " + self.getPhone()
        return info

    def strOut(self):
        info = ""
        info += "Name: " + self.getName() + " Address: " + self.getAddress() + " Age: " + str(
            self.__age) + " Phone: " + self.getPhone()
        return info
