# Class vs. Instance (Hackerrank problem)
class Person:
    def __init__(self,initialAge):
        self.age = initialAge
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if (self.age < 13 and self.age>-1):
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        elif self.age >= 18:
            print("You are old.")
        else:
            self.age = 0
            print(f"Age is not valid, setting age to {self.age}.")
            print("You are young.")
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
            self.age+=1
            return self.age
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")