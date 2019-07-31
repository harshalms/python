'''InterviewBit
Sorted Insert Position
Asked in:  
Yahoo
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0'''
def searchInsert(A, B):
    start, end = 0, len(A)-1
    while start<=end:
        mid = (start+end)//2
        if B == A[mid]:
            return mid
        else:
            if B>A[mid]:
                start = mid+1
            else:
                end = mid-1
    return start

if __name__ == "__main__":
    A =[[1,3,5,6], [1,3,5,6], [1,3,5,6], [1,3,5,6]]
    B=[5, 2, 7, 0]
    for i in range(len(A)):
        print(A[i],",",B[i], "-->", searchInsert(A[i], B[i]))
