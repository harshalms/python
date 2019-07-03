'''GeeksForGeeks
Segregate even and odd numbers | Set 3
Given an array of integers, segregate even and odd numbers in the array. 
All the even numbers should be present first, and then the odd numbers.

Examples:

Input : 1 9 5 3 2 6 7 11
Output : 2 6 5 3 1 9 7 11

Input : 1 3 2 4 7 6 9 10
Output : 2 4 6 10 7 1 9 3
'''
# Time Complexity : O(n)
# Auxiliary Space : O(1)
def evenODD(A):
    for i in range(len(A)):
        while i > 0:
            if A[i]%2 == 0 and A[i-1]%2!=0:
                A[i-1], A[i] = A[i], A[i-1]
            i-=1
    return A
A = [1, 9, 5, 3, 2, 6, 7, 11]
print(evenODD(A))