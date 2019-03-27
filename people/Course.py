import uuid


class Course:
    def __init__(self, name, instructor):
        self.__code = self.__setCode()
        self.__name = name
        self.__instructor = instructor
        self.__credit = None

    # def __init__(self,code, name, instructor):
    #     self.__code = code
    #     self.__name = name
    #     self.__instructor = instructor
    #     self.__credit = None

    def getInstructor(self):
        return self.__instructor

    def getName(self):
        return self.__name

    def getCode(self):
        return self.__code

    def getCredit(self):
        return self.__credit

    def setCredit(self, hours):
        self.__credit = hours

    def setInstructor(self, instructor):
        self.__instructor = instructor

    def setCode(self,code):
        self.__code = code

    def __setCode(self):
        self.__code = str(uuid.uuid4().int)[4::]

    def __str__(self):
        info = self.__code + " " + self.__name + " ( " + self.__instructor + " ) "
        return info