def Sort(A):                   # This is not bubble sort because, in bubble sort we go on
    for i in range(len(A)):          # comparing two adjecent elements, and not one element with all.
        for j in range(i, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                # print(A)
    return A

if __name__=='__main__':
    seq = [5, 3, 8, 6, 7, 2]
    # seq = list(map(int, input().split()))
    print(Sort(seq))