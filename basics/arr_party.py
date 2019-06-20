T = int(input())
for i in range(T):
    N = int(input())
    A=[1, 6]
    for j in range(1, N-1):
        p, q = A[j], A[j-1]
        a = 2*(p + 2) - q
        # A.append(a)
    print(a)