''' 
        Restaurant Selector.py
        pick restaurants based on user's special requests
        Jacob Emory Bullin
        Jan 16, 2019
'''


# define main flow of program
def main():
        isVegetarian, isVegan, isGlutenFree = getRequests()

        restaurants = getRestaurants(isVegetarian, isVegan, isGlutenFree)

        displayRestaurants(restaurants)


# define func's used in main
def getRequests():
        vegetarian = input("Is anyone in your party a vegitarian? (Enter Y or N)")
        vegan = input("Is anyone in your party vegan? (Enter Y or N)")
        glutenFree = input("Is anyone in your party gluten-free? (Enter Y or N)")

        if vegetarian == "y" or vegetarian == "Y":
                isVege = True
        else:
                isVege = False
        if vegan == "y" or vegan == "Y":
                isVega = True
        else:
                isVega = False
        if glutenFree == "y" or glutenFree == "Y":
                isGluFree = True
        else:
                isGluFree = False

        return isVege, isVega, isGluFree


def getRestaurants(isVege, isVega, isGluFree):
        if isVege and isVega and isGluFree:
                restaurants = "R3, R5"
        elif isVege:
                if isVega:
                        restaurants = "R3, R5"
                elif isGluFree:
                        restaurants = "R2, R3, R5"
                else:
                    restaurants = "R2, R3, R4, R5"
        elif isVega:
                restaurants = "R3, R5"
        elif isGluFree:
                if isVega:
                        restaurants = "R3, R5"
                elif isVege:
                        restaurants = "R2, R3, R5"
        else:
                restaurants = "R1, R2, R3, R4, R5"

        return restaurants


def displayRestaurants(result):
        print("Here are your restaurant choices:")
        print(result)


main()
