def BubbleSort(A):
    for i in range(len(A)):
        j = 0
        while j < len(A)-1:
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                # print(A)
            j+=1
    return A
if __name__=='__main__':
    seq = [5, 3, 8, 6, 7, 2]
    # seq = list(map(int, input().split()))
    print(BubbleSort(seq))