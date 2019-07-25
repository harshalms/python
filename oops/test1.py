class Dog:
    # class attribute
    species = 'mammal'
    # Initializer / constructor
    def __init__(self, age):
        self.age = age
# Instantiate the Dog objects
a = Dog(9)
b = Dog(4)
c = Dog(7)
# Determining the oldest Dog
def get_biggest_number(*args):
    return max(args)

print("The oldest Dog is {} years old!!".format(get_biggest_number(a.age, b.age, c.age)))