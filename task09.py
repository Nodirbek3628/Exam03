class Temperatura:
    def __init__(self,celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5)+32
    
temperatura = Temperatura(0)
print(temperatura.celsius)
print(temperatura.fahrenheit)