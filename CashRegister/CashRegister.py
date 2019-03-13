from RetailItem import RetailItem


class Register():
    global inventory

    def __init__(self, i):
        self.__items = i

    def getInventory(self):
        return inventory

    def purchaseItem(self, item, quantity):
        for e in range(len(self.__items)):
            print(self.__items[e].getName())

            if(item == self.__items[e]):
                self.__items[e].sold(quantity)

            ##i = self.__items[e]


def main():
    ##todo: look at tuples in dictionaries. ('k':('val',val))
    r1 = RetailItem("Designer Jeans", 40, 35.95)
    r2 = RetailItem("T-Shirt", 20, 24.95)
    r3 = RetailItem("Jacket", 12, 59.95)
    items = []
    items.append(r1)
    items.append(r2)
    items.append(r3)
    R1 = Register(items)
    print(str(R1.getInventory()))

    R1
