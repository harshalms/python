'''(GeeksForGeeks)
Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed
Given an array, only rotation operation is allowed on array. We can rotate the 
array as many times as we want. Return the maximum possbile of summation of i*arr[i].
Examples :
Input: arr[] = {1, 20, 2, 10}
Output: 72
We can 72 by rotating array twice.
{2, 10, 1, 20}
20*3 + 1*2 + 10*1 + 2*0 = 72

'''

# A = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# A = [1, 20, 2, 10]
A = [8, 3, 1, 2]
def max_array_sum(A):
    max_sum = 0
    for i in range(len(A)):
        temp = A[len(A)-1]
        for j in range(len(A)-1, 0, -1):
            A[j] = A[j-1]
        A[0] = temp
        result = 0
        for k in range(len(A)):
            result+=k*A[k]
        max_sum = max(max_sum, result)
        # print(result)
    return max_sum
# def max_array_sum2(A):
#     result = 0
#     A.sort()
#     for k in range(len(A)):
#             result+=k*A[k]
#     return result

print(max_array_sum(A))
# print(max_array_sum2(A))