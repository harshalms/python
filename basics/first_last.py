'''GeeksForGeeks
Find first and last digits of a number
Given a number and to find first and last digit of a number.
Examples:

Input : 12345 
Output : First digit: 1
         last digit : 5

Input : 98562
Output : First digit: 9
         last digit : 2
'''
def firstLast(A):
    A = str(A)
    return int(A[0]), int(A[-1])
A = 12345
print("First digit:", firstLast(A)[0])
print("Last digit:", firstLast(A)[1])