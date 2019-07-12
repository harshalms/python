'''GeeksForGeeks
Sort an array containing two types of elements
We are given an array of 0s and 1s in random order. 
Segregate 0s on left side and 1s on right side of the array. 
Traverse array only once.

Examples:

Input :  arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output : arr[] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

Input :  arr[] = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1] 
Output : arr[] = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
'''
def sortBinary(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            A[count], A[i] = A[i], A[count]
            count+=1
    return A
if __name__ == "__main__":
    A = [[0, 1, 0, 1, 0, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]]
    for i in range(len(A)):
        print(sortBinary(A[i]))
    