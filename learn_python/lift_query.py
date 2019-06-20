# floors=7
T=int(input("How many Tests? "))
# n=int(input("Call from which floor? "))
A,B=0,7
for i in range(T):
    n=int(input("Call from which floor? "))
    print(A,B)
    if abs(n-A) < abs(n-B):
        print("Lift A will come")
        A=n
        print(A)
    elif abs(n-A) == abs(n-B) and A<B:
        print("Lift A will come")
        A=n
        print(A)
    elif abs(n-A) == abs(n-B) and B<A:
        print("Lift B will come")
        B=n
        print(B)
    else:
        print("Lift B will come")
        B=n
        print(B)