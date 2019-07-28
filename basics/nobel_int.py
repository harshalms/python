"""InterviewBit
Given an integer array, find if an integer p exists in the array such 
that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1."""
def solve(A):
    A.sort()
    nobel = {}
    A.sort()
    for i in range(len(A)):
        if A[i] == len(A)-i-1:
            if i == len(A)-1:
                return 1
            elif A[i] < A[i+1]:
                return 1
            else:
                return -1
    return -1

# A = [7, 3, 16, 10, 7, 7, 10, 3, -1, 0]
A = [ -2, 8, 8, 6, -2, 3, -2, -7, 3, 3, -2, 0, 4, -3, -4, -2, -1, -10, -4, -2, 7, -1, 0, -7, 3, -7, 7, 3, 2, -4, -5, 2, 6, 5, -2, 7, -1, 6, -10, 4, -9, -10, -6, -2, -3, 0, -2, 6, -8, 4, 7, 9, -7, 9, -8, -2, -7, -10, -9, -3, 8, 9, 1, 5, 4, 9, 2, 5, -3, -6, -1, -1, -6 ]
# A = [-1, -9, -2, -78, 0]
print(solve(A))