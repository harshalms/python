# s1=input("Enter first string? ")
# s2=input("Enter second string? ")
T=int(input())

def compare(A,B):
    dictA, dictB={}, {}
    for i in A:
        if i in dictA:
            dictA[i]+=1
        else:
            dictA[i]=1
    for i in B:
        if i in dictB:
            dictB[i]+=1
        else:
            dictB[i]=1
    if dictA == dictB:
        return True
    else:
        return False

for i in range(T):
    s1=input().split(" ")
    print(s1)
    # s2=input()
    if compare(s1[0],s1[1]):
        print("YES")
    else:
        print("No")
