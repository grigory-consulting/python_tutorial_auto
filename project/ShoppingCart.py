from Product import Product
#import Product


class ShoppingCart:

    def __init__(self):
        self.items = {} # Dictionary keys are Product, values quantities 

    def __repr__(self):
        return f"ShoppingCart({self.items})"


    def clear(self):
        self.items.clear()

    def delete(self, product):
        del self.items[product]

    def add(self, product, q=1):
        if q <= product.quantity:
            self.items[product] = self.items.get(product,0) + q
    # TODO later plus_one, minus_one for the buttons

    def total_price(self):

        total = 0
        for product in self.items:
            total += product.price * self.items[product] # price x how many are in cart

        return total 

if __name__ == "__main__":
    product1 = Product("001", "1", 20.99, 5)
    product2 = Product("002", "2", 19.99, 2)
    cart = ShoppingCart()
    cart.add(product1)
    cart.add(product2,2)
    print(cart.items)
    print(cart.total_price())
    