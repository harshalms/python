def insertion_sort(A):
    for i in range(len(A)):
        j=i
        while j>0 and A[j]<A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j-=1
    return A        

if __name__ == "__main__":
    A = [74, 32, 32, 58, 64, 21, 64]
    # A = [1, 2, 3, 4, 5]
    print(insertion_sort(A))