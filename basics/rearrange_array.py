# A = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
# A = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
A = [9, 6, 5, 3, 4, 2, -1, 0, 1, 8]

def rearrange(A):
    for i in range(len(A)):
        if A[i] != -1 and A[i] != i:
            print(i, A[i])
            temp = A[i]
            A[i] = A[A[i]]
            A[temp] = temp
            
            print(A)
    return A
print(rearrange(A))