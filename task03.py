class Animal:

    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"Woof! Woof! ")
    

dog = Dog("Rex")
print(dog.name)
dog.bark()