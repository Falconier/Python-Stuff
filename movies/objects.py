class Movie:
    def __init__(self, id=0, name=None, year=0, minutes=0, category=None):
        self.id = id
        self.name = name
        self.year = year
        self.minutes = minutes
        self.category = category

    def getName(self):
        return self.name

    def getID(self):
        return self.id

class Category:
    def __init__(self, id=0, name=None):
        self.id = id
        self.name = name

