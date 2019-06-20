A=[1, 2, 4, 3, 8, 5, 3]
max, max2 = A[0], A[0]
for i in A:
    if max < i:
        max2 = max
        max = i
    if max2 < i and i < max:
        max2 = i
print(max2)