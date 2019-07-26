# parent class
class Pets:
    dogs = []
    def __init__(self, dogs):
        self.dogs = dogs
    
# parent class
class Dog:
    # class attribute
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungery = True

    def eat(self):
        self.is_hungery = False
    def walk(self):
        return "{} is walking!".format(dog.name)

# creating instance
my_dogs = [Dog("Tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]
# instantiate the pets class
my_pets = Pets(my_dogs)
print("I have {} dogs.".format(len(my_dogs)))
for dog in my_dogs:
    dog.eat()
    print('{} is {}.'.format(dog.name, dog.age))
    print(dog.walk())
print("And they are all {}, off course.".format(dog.species))

are_my_dogs_hungery = False
for dog in my_dogs:
    if dog.is_hungery:
        are_my_dogs_hungery = True
if are_my_dogs_hungery:
    print("My dogs are hungery")
else:
    print("my dogs are not hungery.")
