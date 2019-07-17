def maxArr(A):
    max_sum, total = 0, 0
    for i in range(1, len(A)):
        for j in range(i+1, len(A)+1):
            total = abs(A[i-1] - A[j-1]) + abs(i - j)
            max_sum = max(max_sum, total)
    # maximum, minimum = A[0], A[0]
    # i, j = 0, 0
    # for k in range(len(A)):
    #     if A[k] > maximum:
    #         maximum = A[k]
    #         i = k+1
    #     if A[k] < minimum:
    #         minimum = A[k]
    #         j = k+1
    # max_sum = abs(maximum-minimum) + abs(i-j)
    return max_sum
# A = [3, -2, 5, -4]
# A = [1, 3, -1]
A = [2, 2, 2]
print(maxArr(A))