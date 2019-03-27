##region File information
# define product class
# 3/27/19
##endregion

class Product:
    def __init__(self):
        pass

    def __init__(self, code, description, quantity, price):
        self.code = code
        self.__description = description
        self.__quant = quantity
        self.price = price

    def getCode(self):
        return self.code

    def setCode(self, c):
        self.code = c

    def getDescription(self):
        return self.__description

    def setDiscription(self, d):
        self.__description = d

    def getQuantity(self):
        return self.__quant

    def setQuantity(self, q):
        self.__quant = q

    def getPrice(self):
        return self.price

    def setPrice(self, p):
        self.price = p

    def __str__(self):
        info = "Product Code: " + self.code
        info += "Product Description: " + self.__description
        info += "Quantity: '" + self.__quant
        info += "Price: " + self.price
        return info
