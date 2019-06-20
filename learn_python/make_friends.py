N = int(input("Total people? "))
X = int(input("At least required skills? "))

for i in range(N):
    Y=int(input("Number of skills? "))
    if Y>=X:
        print("YES")
    else:
        print("NO")