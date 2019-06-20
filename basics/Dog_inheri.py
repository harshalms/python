class Pets:
    dogs=[]
    def __init__(self, dogs):
        self.dogs = dogs



class Dogs:
    species = "mammals"
    def __init__(self, name, age):
        tom = Pets("Tom", 6)
        fletcher = Pets("Fletcher", 7)
        larry = Pets("Larry", 9)
        print(larry.name, larry.age)