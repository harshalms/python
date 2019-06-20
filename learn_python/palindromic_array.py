# A=[1, 2, 3, 4, 3, 2, 1]
A='nitind'
# i, j = 0, len(A)-1
def palindrom(A):
    i, j = 0, len(A)-1
    while(i<=j):
        if A[i] != A[j]:
            return False
        i=i+1
        j=j-1
    else:
        return True
print(palindrom(A))