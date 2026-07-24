from Product import Product
from datetime import date


class Food(Product):

    def __init__(self, id, name, price, quantity, expired_by):
        super().__init__(id, name, price, quantity)
        self.expired_by = expired_by
    

if __name__ == "__main__": 
    d = date(2026,8,30)
    tomato = Food("002", "Tomato", 1.49, 2, d)
    print(tomato)
