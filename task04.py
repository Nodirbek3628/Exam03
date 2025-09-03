class Flyer:

    def fly(self):
        print("Duck is flying")

class Swimmer:

    def swim(self):
        print("Duck is swimming")


class Duck(Swimmer,Flyer):
    pass

duck = Duck()
duck.fly()
duck.swim()
