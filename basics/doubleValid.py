'''GeeksForGeeks
Double the first element and move zero to end.
Given an array of integers of size n. Assume ‘0’ as invalid number and all other 
as valid number. Convert the array in such a way that if next valid number is 
same as current number, double its value and replace the next number with 0. 
After the modification, rearrange the array such that all 0’s are shifted to the end.
Examples:

Input : arr[] = {2, 2, 0, 4, 0, 8}
Output : 4 4 8 0 0 0

Input : arr[] = {0, 2, 2, 2, 0, 6, 6, 0, 0, 8}
Output :  4 2 12 8 0 0 0 0 0 0
Source: Microsoft IDC Interview Experience | Set 150.
Time complexity: O(2*n)
'''
def doubleValid(A):
    count = 0
    for i in range(len(A)-1):
        if A[i]!=0 and A[i]==A[i+1]:
            A[i], A[i+1] = 2*A[i], 0
    for i in range(len(A)):
        if A[i]!=0:
            A[count], A[i] = A[i], A[count]
            count+=1 
    return A
if __name__ == "__main__":
    A = [[2, 2, 0, 4, 0, 8], [0, 2, 2, 2, 0, 6, 6, 0, 0, 8],[4]]
    for i in range(len(A)):
        print(doubleValid(A[i]))