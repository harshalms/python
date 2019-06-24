# Binary search by recursion method.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key = 3
def BinSearch(A, start, end, x):
    # print(start, end, x)
    if start == end:
        if A[start] == x:
            return start
        else:
            print('hi')
            return False
    else:
        mid = (start+end)//2
        if A[mid] == x:
            return mid
        elif A[mid] < x:
            return BinSearch(A, mid + 1, end, x)
        else:
            return BinSearch(A, start, mid - 1, x)
    return 0
start, end = 0, len(A)-1
print(BinSearch(A, start, end, key))