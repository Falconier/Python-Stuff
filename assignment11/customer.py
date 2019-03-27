#region File Information
# customer.py
# Jacob Emory Bullin
##endregion

from assignment11.person import Person

class Customer(Person):
    def __init__(self, name, address, age, phoneNum, CustNumber, mailing):
        super().__init__(name, address, age, phoneNum)
        self.__cNum = CustNumber
        self.__mailList = mailing

    def getCustomerNumber(self):
        return self.__cNum

    def getMailingList(self):
        return self.__mailList

    def setCustomerNumber(self, custNumber):
        self.__cNum = custNumber

    def setMailingList(self, getMail):
        self.__mailList = getMail

    def __str__(self):
        info = super().strOut()
        info += " Cusotmer Number: " + str(self.getCustomerNumber()) + " Mailing List: " + str(self.getMailingList())
        return info