from Car import Car


def main():
    cars = []

    # for i in range(5):
    car1 = Car("1111","Honda", "CRZ", 2011,"Gray", "5000")
    car2 = Car("2222","Honda","Civic", 2008,"Red", "4000")
    car3 = Car("3333", "Honda", "Accord", 2008, "White", "4000")
    car4 = Car("4444", "Honda", "Pilot", 2012, "Blue", "8000")
    cars.append(car1)
    cars.append(car2)
    print(car1)
    print(car2)
    # print(cars)

main()