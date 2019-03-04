##File Information
# Student.py
# Resources to manage a student's name and test scores.
##endregion

class Student():
    def __init__(self, name, number):
        self.__name = name
        self.__scores = []
        for count in range(number):
            self.__scores.append(0)
        self.__average = self.getAverage()

    def getName(self):
        return self.name

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
        return "Name:" + __Nm + "\nScores: " + __avg + "\n"

    ##region New Code

    def __gt__(self, other):
        return self.getAverage() > other.getAverage()

    def __lt__(self, other):
        return self.getAverage() > other.getAverage()

    def __eq__(self, other):
        return self.getAverage() == other.getAverage()

    def __ne__(self, other):
        return not self.getAverage() == other.getAverage()

    def __le__(self, other):
        return self.getAverage() <= other.getAverage()

    def __ge__(self, other):
        return self.getAverage() >= other.getAverage()

    ##endregion


def main():
    s1 = Student("A", 3)
    s2 = Student("B", 3)

    s1.setScore(1,100)
    s1.setScore(2,98)
    # s1.setScore(3,75)
    s1.setScore(3,85)


    s2.setScore(1,100)
    s2.setScore(2,98)
    s2.setScore(3,75)
    # s2.setScore(3,85)

    print(s1)
    print(s2)

    print("s1 equal to s2:", s1 == s2)
    print("s1 less than s2:", s1 < s2)
    print("s1 greater than or equal to s2:", s1 >= s2)

    # print("s1 not equal to s2:", s1 != s2)
    # print("s1 greater than s2:", s1 > s2)
    # print("s1 less than or equal to s2:", s1 <= s2)


main()