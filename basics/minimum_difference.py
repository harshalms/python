'''GeeksForGeeks
Find minimum difference between any two elements
Given an unsorted array, find the minimum difference between any pair in given array.
Examples :

Input  : {1, 5, 3, 19, 18, 25};
Output : 1
Minimum difference is between 18 and 19

Input  : {30, 5, 20, 9};
Output : 4
Minimum difference is between 5 and 9

Input  : {1, 19, -4, 31, 38, 25, 100};
Output : 5
Minimum difference is between 1 and -4
'''
def minDifference(A):
    A.sort()
    mini = max(A)
    for i in range(len(A)-1):
        diff = A[i+1] - A[i]
        mini = min(mini, diff)
    return mini
if __name__ == "__main__":
    A = [[1, 5, 3, 19, 18, 25], [30, 5, 20, 9], [1, 19, -4, 31, 38, 25, 100]]
    for i in range(len(A)):
        print(minDifference(A[i]))
