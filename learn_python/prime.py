import math
N = int(input("Enter a Number "))
root = int(math.sqrt(N))
def prime(n, root):
    root = int(math.sqrt(n))
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2, root+1):
        if n % i == 0:
            return False
    return True
if prime(N, root):
    print("Prime Number")
# elif n==2:
#     print("Prime Number")
else:
    print("Not a Prime number")

for j in range(2, N+1):
    if prime(j, root) :
        print(j, end=",")
