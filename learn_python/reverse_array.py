A = [4, 5, 1, 2]
def reverseArray(A):
    i, j = 0, len(A)-1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i+=1
        j-=1
    return A
print(reverseArray(A))