class Cart:
    def __init__(self):
        self.pricec = []

    def add_item(self,name,price):
        self.name = name
        self.price = price

        if price not in self.pricec:
            self.pricec.append(price)

    def get_total(self):
        summ = 0
        for price in self.pricec:
            summ += price
        
        return summ
        
    
cart = Cart()
cart.add_item("Laptop", 2000)
cart.add_item("Mouse", 100)
print(cart.get_total())