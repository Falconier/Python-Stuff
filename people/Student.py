from people import Person
from Course import Course
import uuid

class Student(Person):

    def __init__(self,name, dob, courses):
        super().__init__(name,dob)
        self.__id = uuid.uuid4().hex
        self.__courses = courses
        # self.__courses = self.__courses.extend(courses)

    def getID(self):
        return str(self.__id)

    def getCourses(self):
        return self.__courses

    def setCourses(self,courses):
        self.__courses = []
        self.__courses.extend(courses)

    def addCourses(self, courses):
        self.__courses.append(courses)

    def dropCourse(self, course):
        if(course in self.__courses):
            self.__courses.remove(course)

    def __str__(self):
        info = "Name:" + super().getName() + "\nID:"+ str(self.__id) +"\nCourses Taken:"+ str(self.__courses)
        return info


def main():
    c1 = Course("Python", "Zhang")
    print(c1)
    c2 = Course("Java", "Zhang")
    print(c2)
    s1 = Student("s1", "01012001", [c1,c2])

    print(s1)
    # print(s1.getID())

main()