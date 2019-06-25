'''GeeksForGeeks
Find the Rotation Count in Rotated Sorted array
Consider an array of distinct numbers sorted in increasing order. 
The array has been rotated (clockwise) k number of times. Given such an array, 
find the value of k.
Approch : Just find the index of minimum element.
'''
A = [15, 18, 2, 3, 6, 12]
def indexOFmin(A):
    min = A[0]
    for i in range(len(A)):
        if min > A[i]:
            min, k = A[i], i
    return k
print(indexOFmin(A))
