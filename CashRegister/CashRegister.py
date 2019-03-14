##region Assignment Information
# CashRegister.py
# Jacob Emory Bullin
# allows transactions of retail items objects
##endregion

from RetailItem import RetailItem

class Register():
    def __init__(self, inventory):
        self.__inventory = inventory
        self.__purchaseOrder = []
        self.__total = 0.0

##region Methods
    def getInventory(self):
        return str(self.__inventory)

    def getPurchaseOrder(self):
        order = ""
        for e in self.__purchaseOrder:
            order += str(e).title() + "\n"
        return order

    def sellItem(self, item):
        hasItem = True
        for e in self.__inventory:
            if (item.title() == e.getName().title()):
                if (e.getQuantity() > 0):
                    hasItem = True
                    e.sold(1)
                    self.__purchaseOrder.append(item)
                    self.__total += e.getPrice()
                    break
                else:
                    print("We are currently out of " + e.getName() + "'s.")
                    hasItem = True
            else:
                hasItem = False
                ##todo: fix this because it doesnt work
        if (not hasItem):
            print("We dont not have any " + item + "'s here.")

    def clearOrder(self):
        for e in self.__purchaseOrder:
            for f in self.__inventory:
                if(e.getName().title() == f.getName().title()):
                    f.returned(1)
                    self.__total -+ f.getPrice()
                    # self.__purchaseOrder.remove(e)
                    break
        self.__purchaseOrder.clear()
        if(self.__total != 0):
            self.__total = 0

    def getTotal(self):
        return self.__total
##endregion


def main():
    r1 = RetailItem("Jeans", 25, 24.99)
    r2 = RetailItem("T-Shirt", 23, 12.99)
    r3 = RetailItem("Jacket", 2, 19.99)

    inven = [r1, r2, r3]

    R1 = Register(inven)

    # print(R1.getInventory())
    while (True):
        itm = str(input("Item Name (End to pay): "))
        if (itm.upper() != "END"):
            R1.sellItem(itm)
        else:
            break
    print("Items Purchased:")
    print(R1.clearOrder())
    print(R1.getPurchaseOrder())
    print("Total: $", R1.getTotal())


main()
