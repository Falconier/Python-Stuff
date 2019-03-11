##region File Information
# Student.py
# Resources to manage a student's name and test scores.
##endregion

class Student():
    ##region class information
    def __init__(self, name, number):
        self.__name = name
        self.__scores = []
        for count in range(number):
            self.__scores.append(0)
        self.__average = self.getAverage()

    def getName(self):
        return self.__name

    def setScore(self, i, score):
        self.__scores[i-1] = score
        # Modification
        self.__average = self.getAverage()

    def getScore(self, i):
        return self.__scores[i-1]

    def getAverage(self):
        return sum(self.__scores) / len(self.__scores)

    def getHighScore(self):
        return max(self.__scores)


    def __str__(self):
        self.__average = self.getAverage()
        __avg = str(self.__average)
        __Nm = str(self.__name)

        __Sc = self.__scores

        stR = ""

        for i in range(len(__Sc)):
            stR = stR + str(__Sc[i]) + ","

        return "Name:" + __Nm + "\nScores: " + str(self.getAverage())+ "\n" + stR.rstrip(",")
    ##endregion

    ##region New Code

    def __gt__(self, other):
        return self.getName() > other.getName()

    def __lt__(self, other):
        return self.getName() < other.getName()

    def __eq__(self, other):
        return self.getName() == other.getName()

    def __ne__(self, other):
        return not self.getName() == other.getName()

    def __le__(self, other):
        return self.getName() <= other.getName()

    def __ge__(self, other):
        return self.getName() >= other.getName()

    def equalTo(self, other):
        return self.getName() == other.getName()

    def lessThan(self, other):
        return self.getName() < other.getName()

    def greaterOrEqualTo(self, other):
        return self.getName() >= other.getName()

    ##endregion

    ##region Title

    ##endregion

def main():
    s1 = Student("s1", 3)
    s2 = Student("s2", 3)

    ##region Other print statements that are not used
    # s1.setScore(1,100)
    # s1.setScore(2,98)
    # # s1.setScore(3,75)
    # s1.setScore(3,85)
    #
    #
    # s2.setScore(1,100)
    # s2.setScore(2,98)
    # s2.setScore(3,75)
    # s2.setScore(3,85)

    # print("s1 equal to s2:", s1.getName() == s2.getName())
    # print("s1 less than s2:", s1 < s2)
    # print("s1 greater than or equal to s2:", s1 >= s2)

    ##endregion no

    print(s1)
    print(s2)

    print("Name compare (equal to):", s1.equalTo(s2))
    print("Name compare (less than):", s1.lessThan(s2))
    print("Name compare (greater than or equal to):", s1.greaterOrEqualTo(s2))

    # print("s1 not equal to s2:", s1 != s2)
    # print("s1 greater than s2:", s1 > s2)
    # print("s1 less than or equal to s2:", s1 <= s2)


main()