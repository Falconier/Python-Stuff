#region File Information
# Jacob Bullin, Troy Choplin
# rectangleCalculator.py
# 3/25/19
#endregion

class Rectangle:
    def __init__(self, height, width):
        self.__height = int(height)
        self.__width = int(width)

    def calcPerimeter(self):
        h = self.__height
        w = self.__width
        return (2*h)+(2*w)

    def calcArea(self):
        h = self.__height
        w = self.__width
        return (h*w)

    def printRectangle(self):
        h = self.__height
        w = self.__width
        prnt = ""
        for i in range(h):
            for j in range(w):
                if (i == 0 or i == h-1):
                    prnt += '* '
                elif (i != 0 and (j == 0 or j == w-1)):
                    prnt += '* '
                elif (not (i == 0 or i == h-1)):
                    prnt += '  '
                elif (not (i != 0 and (j == 0 or j == w-1))):
                    prnt += '  '
            print(prnt)
            prnt = ""

def main():
    print("Rectangle Calculator")
    while(True):
        h = input("Height: ")
        w = input("Width: ")
        r = Rectangle(h,w)
        print("Perimeter:", r.calcPerimeter())
        print("Area:", r.calcArea())
        r.printRectangle()
        cont = input("Continue (Y/N)? ").upper()
        if(cont=="N"):
            break

main()