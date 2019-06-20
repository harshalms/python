i=1
while(i<=3):
    number = int(input("Guess a number? "))
    if number==9:
        print("You Won!!!")
        break
    i=i+1
if i>3:
    print("You Loose!")