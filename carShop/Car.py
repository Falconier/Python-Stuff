##region File Information
# Car.py
# Vin, Make, Model, Year, Color, and price
##endregion


class Car:
    def __init__(self, vin, make, model, year, color, price):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        self.__price = price

    ##region Gets
    def getVin(self):
        return self.__vin

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getYear(self):
        return self.__year

    def getColor(self):
        return self.__color

    def getPrice(self):
        return self.__price
    ##endregion

    ##region Sets
    def setVin(self,vin):
        self.__vin = vin

    def setMake(self,make):
        self.__model = make

    def setModel(self,model):
        self.__model = model

    def setYear(self, year):
        self.__year = year

    def setColor(self, color):
        self.__color = color

    def setPrice(self, price):
        self.__price = price
    ##endregion

    ##region Overides
    def __str__(self):
        return "Vin: " + self.__vin + "\nMake: " + self.__make + "\n"

    ##endregion
