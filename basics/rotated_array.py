'''InterviewBit
Rotated Array
Asked in: Facebook
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array will not contain duplicates.'''
def findMin(A):
    if len(A) == 0:
        return -1

    start, end = 0, len(A)-1
    
    while start < end:
        mid = (start+end) // 2
        if A[mid] < A[end]:
            end = mid
        else:
            start = mid + 1
            
    return A[end]

if __name__ == "__main__":
    A = [4, 5, 6, 7, 0, 1, 2, 3]
    print("Minimum value in array:", findMin(A))