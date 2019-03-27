#region File Information
# testerFile.py
# Jacob Emory Bullin
##endregion
from assignment11.person import Person
from assignment11.customer import Customer


def main():
    p1 = Person("Jacob Bullin", "1234 Null Ave, Nowhere, OK", 21, "123-456-7890")
    p2 = Person("Tim Cook", "1 Infinite Loop, Cupertino, CA", 58, "800-692-7753")
    p3 = Person("John Smith", "4321 Void Way, Suix Falls, ID", 31, "208-123-4567")

    c1 = Customer(p3.getName(),p3.getAddress(),p3.getAge(), p3.getPhone(),1,False)

    print(p1)
    print(p2)
    print(p3)

    print(c1)

main()