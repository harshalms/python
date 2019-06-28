'''(GeeksForGeeks)
Move all zeroes to end of array.
Given an array of random numbers, Push all the zero’s of a given 
array to the end of the array. For example, if the given arrays 
is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed 
to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. 
Expected time complexity is O(n) and extra space is O(1).
'''
# A = [1, 2, 0, 4, 3, 0, 5, 0]
# A = [1, 2, 0, 0, 0, 3, 6]
A = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
def moveZERO(A):
    count, k = 0, 0
    for i in range(len(A)):
        if A[i]!=0:
            A[k]=A[i]
            k+=1
    for k in range(k, len(A)):
        A[k]=0
    return A
print(moveZERO(A))