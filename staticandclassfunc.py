class person (object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

        @classmethod #we can call it without creating an instance
        def getPopulation(cls):
            return cls.population

        @staticmethod #don't need self, we can call it without creating instance
        def isAdult(age):
            return age >= 18

        def display(self):
            print(self.name, 'is', self.age, 'years old')

newPerson = person('Tim', 18)