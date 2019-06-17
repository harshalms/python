A = [1, 2, 3, 4, 5, 6, 99, 109, 111]
x=1
def bin_search(A):
    start, end = 0, len(A)-1
    while start <= end:
        mid = (start + end)//2
        if x == A[mid]:
            return mid
        else:
            if x < A[mid]:
                end = mid-1
            else:
                start = mid+1
    return False
print(bin_search(A))