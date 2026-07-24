

class Product:

    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product({self.id}, {self.name},{self.price:.2f}, {self.quantity})"

    def __str__(self):
        return f"Product({self.id}, {self.name}, {self.price:.2f}, {self.quantity})"

    def stock_up(self, q):
        if q>0 and isinstance(q,int): 
            self.quantity += q
        else:
            print("q must be non-negative integer") # TODO later we will raise an error 

    def buy(self,q):
        if q>0 and isinstance(q,int) and self.quantity>=q:
            self.quantity -= q
        else: 
            print("q must be non-negative integer and be in stock") # TODO raise an error 



if __name__ == "__main__": # check whether you are in entry point 
    product1 = Product("001", "test_name", 20.99, 5)
    print(product1)
    product1.stock_up(20)
    product1.buy(10)
    print(product1)