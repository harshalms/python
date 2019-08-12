'''GeeksForGeeks
Find the smallest missing number.
Given a sorted array of n distinct integers where each integer is in the 
range from 0 to m-1 and m > n. Find the smallest number that is missing from the array.

Examples
Input: {0, 1, 2, 6, 9}, n = 5, m = 10
Output: 3

Input: {4, 5, 10, 11}, n = 4, m = 12
Output: 0

Input: {0, 1, 2, 3}, n = 4, m = 5
Output: 4

Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11
Output: 8'''
# Time Complexity: O(n)
def FindMissing(A):
    for i in range(len(A)-1):
        if A[i+1]-A[i]>1:
            return A[i]+1
    return A[len(A)-1]+1
# Using Binary Search
# def FindMissingBinary(A):
#     for i in range(len(A)+1):
#         start, end = 0, len(A)-1
#         while start <= end:
#             mid = (start + end)//2
#             if i == A[mid]:
#                 return i
#                 # count = 0
#             else:
#                 if i < A[mid]:
#                     end = mid-1
#                 else:
#                     start = mid+1
#         return ("No",i)
#     # return i
                
# A = [0, 1, 2, 6, 9]
# print(FindMissingBinary(A))

if __name__ == "__main__":
    arr = [[0, 1, 2, 6, 9], [0, 1, 2, 3], [0, 1, 2, 3, 4, 5, 6, 7, 10]]
    for i in range(len(arr)):
        print(arr[i],"---->", FindMissing(arr[i]))
        # print(arr[i],"---->", FindMissingBinary(arr[i]))
        # print()