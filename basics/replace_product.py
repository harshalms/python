'''GeeksForGeeks
Replace every array element by multiplication of previous and next
Given an array of integers, update every element with multiplication 
of previous and next elements with following exceptions. 
a) First element is replaced by multiplication of first and second.
b) Last element is replaced by multiplication of last and second last.

Example:

Input: arr[] = {2, 3, 4, 5, 6}
Output: arr[] = {6, 8, 15, 24, 30}

// We get the above output using following
// arr[] = {2*3, 2*4, 3*5, 4*6, 5*6} '''
def replace_with_product(A):
    B = [0]*len(A)
    for i in range(1, len(A)-1):
        B[i] = A[i-1]*A[i+1]
    B[0], B[len(A)-1] = A[0]*A[1], A[len(A)-2]*A[len(A)-1]
    return B
#  Time complexity of this solution is O(n), but it requires O(n) extra space.
def replace_with_product2(A):
    prev = A[0]
    A[0] = A[0]*A[1]
    for i in range(1, len(A)-1):
        curr = A[i]
        A[i] = prev*A[i+1]
        prev = curr
    A[len(A)-1] = prev*A[len(A)-1]
    return A
#  Time complexity of this solution is O(n), and space complexity is O(1).
A = [2, 3, 4, 5, 6]
print(replace_with_product(A))
print(replace_with_product2(A))
