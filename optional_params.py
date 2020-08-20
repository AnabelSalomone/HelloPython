# Optional Parameters
# Second parameter becomes optional

def func(word, freq=3):
    print(word*freq)

call = func('hello')
# hellohellohello


class car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self, showAll=True):
        if showAll:
            print("This car is a %s %s from %s" %(self.make, self.model, self.year))
        else:
            print("This car is a %s %s" %(self.make, self.model))


whip = car("Ford", "Fusion", 2012)
whip.display()