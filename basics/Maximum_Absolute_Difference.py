def maxArr(A):
    max_sum, total = 0, 0
    for i in range(1, len(A)):
        for j in range(i+1, len(A)+1):
            total = abs(A[i-1] - A[j-1]) + abs(i-j)
            max_sum = max(max_sum, total)
    # maximum, minimum = (A[0], 1), (A[0], 1)
    # for k in range(len(A)):
    #     set1 = (A[k], k+1)
    #     if set1 > maximum:
    #         maximum = max(maximum, set1)
    #     if set1 < minimum:
    #         minimum = min(minimum, set1)
    # print(maximum, minimum)
    # max_sum = abs(maximum[0]-minimum[0]) + abs(maximum[1]-minimum[1])
    return max_sum
# A = [3, -2, 5, -4]
# A = [1, 3, -1]
# A = [2, 2, 2]
A = [ 55, -8, 43, 52, 8, 59, -91, -79, -18, -94 ]
print(maxArr(A))