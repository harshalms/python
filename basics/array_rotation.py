A = [1, 2, 3, 4, 5, 6, 7]
d = 2
def rotate1(A, d):
    b = A[:d]
    c = A[d:]
    b.reverse()
    c.reverse()
    A = b + c
    A.reverse()
    return A
def rotate2(A, d):
    A = A[d:] + A[:d]
    return A
def cylindrical_rotate(A, d):
    for j in range(len(A)-d):
        temp = A[-1]
        for i in range(len(A)-1, 0, -1):
            A[i] = A[i-1]
        A[0] = temp
    return A

print(rotate1(A, d))
print(rotate2(A, d))
print(cylindrical_rotate(A, d))