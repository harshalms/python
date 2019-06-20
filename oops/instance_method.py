class Laptop:
    # class variable can be used if any repeated variable is there for each object
    discount_percent = 15
    def __init__(self, brand, model, price):
        # instance variables
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + ' ' + model
    def discount(self):
        return (self.price - self.price*Laptop.discount_percent/100) #class variabes are used with class name.var
# objects
L1 = Laptop("Sony", "i3", 40000)
L2 = Laptop("Dell", "i5", 45000)

# print(L1.brand)
# print(L2.laptop_name)
print(L1.discount())
# actually above statement calls the class in which method discount is defined, and then it get into
# the function itself and get excuted.
#  We can write above statemnt in  another way
print(Laptop.discount(L2))
print(L1.__dict__) # gives every instances of L1 with their values