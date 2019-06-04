for i in range(6):
    for j in range(7):
        if (((i+j)%3 !=0)and i==0) or ((j%3 ==0) and i==1) or (i-j==2) or (i+j==8):
            print('*', end=" ")
        else:
            print(end="  ")
    print()