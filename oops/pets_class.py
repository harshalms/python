class Dog:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungery = True

    def eat(self):
        self.is_hungery = False
        
class Pets(Dog):
    def description(self):
        return "{0} is {1}".format(self.name, self.age)
Tom = Pets("Tom", 6)
Fletcher = Pets("Fletcher", 7)
Larry = Pets("Larry", 9)

def call_description(*args):
    print("I have {} dogs".format(len(args)))
    print(Tom.description())
    print(Fletcher.description())
    print(Larry.description())
    print("And they are all mammals, off course.")
call_description(Tom, Fletcher, Larry)
def hungery(*args):
    for i in 
print(Tom.is_hungery)
Tom.eat()
print(Tom.is_hungery)