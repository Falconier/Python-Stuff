##region Assignment Information
# RetailItem.py
# Jacob Emory Bullin
# retail item object
##endregion

class RetailItem():

    def __init__(self, itemName, quanntity, price):
        self.name = itemName
        self.quant = quanntity
        self.price = price

    ##region Gets and Sets
    def setItemName(self, name):
        self.name = name

    def setQuatity(self, amount):
        self.quant = amount

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quant

    def getPrice(self):
        return self.price

    def sold(self, quantity):
        self.setQuatity(self.getQuantity() - quantity)

    def returned(self, quantity):
        self.setQuatity(self.getQuantity() + quantity)
##endregion

# def main():
#     r1 = RetailItem("Jeans", 25, 24.99)
#     r2 = RetailItem("T-Shirt", 23, 12.99)
#     r3 = RetailItem("Jacket", 12, 19.99)
#
#     print(r1.getName())
#     print(r2.getName())
#     print(r3.getName())
#
#
# main()
