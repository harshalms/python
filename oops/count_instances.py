class Automobiles:
    pass
    count_instance = 0
    def __init__(self): # to count instanes we can count no. of times init being called
        Automobiles.count_instance+=1

car1 = Automobiles()
car2 = Automobiles()
car3 = Automobiles()
print()
print(Automobiles.count_instance)