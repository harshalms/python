def InsertionSort(A):
    for i in range(len(A)):
        pos = i
        while pos>0 and A[pos]<A[pos-1]:
            A[pos], A[pos-1] = A[pos-1], A[pos]
            pos-=1
    return A
if __name__=='__main__':
    # seq = [74, 32, 32, 58, 64, 21, 64]
    # seq = [1, 2, 3, 4, 5]
    seq = list(map(int, input().split()))
    print(InsertionSort(seq))