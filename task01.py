class Car:
    def __init__(self,brand,model,year):
        self.brand = brand 
        self.model = model
        self.year = year

    def get_info(self):
        print(f"{self.brand} {self.model} ({self.year})")

car = Car("Chevrolet","Cobalt",2023)
car.get_info()
