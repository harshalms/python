A=[1, 2, 4, 3, 8, 5, 0]
max, min = A[0], A[0]
for i in A:
    if max < i:
        max = i
    if min > i:
        min = i

print(max, min)