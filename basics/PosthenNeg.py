'''GeeksForGeeks
Move all negative elements to end in order with extra space allowed
Given an unsorted array of both negative and positive integer. 
The task is place all negative element at the end of array without 
changing the order of positive element and negative element.
Examples:

Input : arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output : 1  3  2  11  6  -1  -7  -5 

Input : arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
Output : 7  9  10  11  -5  -3  -4  -1 
'''
# Time Complexity : O(n)
# Auxiliary space : O(1)
def PosNegArrange(A):
    for i in range(len(A)):
        j = i
        while j>0:
            if A[j]>=0 and A[j-1]<0:
                A[j-1], A[j] = A[j], A[j-1]
            j-=1
    return A
if __name__ == "__main__":
    A = [[12, 11, -13, -5, 6, -7, 5, -3, -6], [-12, 11, 0, -5, 6, -7, 5, -3, -6], 
    [1, -1, 3, 2, -7, -5, 11, 6], [-5, 7, -3, -4, 9, 10, -1, 11]]
    for i in range(len(A)):
        print(PosNegArrange(A[i]))