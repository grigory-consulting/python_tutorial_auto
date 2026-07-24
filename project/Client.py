

from Product import Product
from ShoppingCart import ShoppingCart

class Client: 
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cart = ShoppingCart() 

    def __repr__(self):
        return f"Client({self.id}, {self.name})"

    def order(self):
        # return will be total_price 
        if not self.cart.items:
            return 0.0 # marks also end of function 

        total = self.cart.total_price()

        for product in self.cart.items:
            q = self.cart.items[product] # how many in cart
            product.buy(q) 

        # empty the cart
        self.cart.clear() 

        return total

if __name__ == "__main__":
    laptop = Product("001", "laptop", 999.99, 5)
    anna = Client("u001", "Anna")
    anna.cart.add(laptop,5)
    print(anna.cart)
    print(laptop.quantity) 
    total = anna.order()
    print(anna.cart)
    print(laptop.quantity)
    print(total)
    print(anna)

