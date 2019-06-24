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
    b = A[:d]
    c = A[d:]
    A = c + b
    return A

print(rotate1(A, d))
print(rotate2(A, d))