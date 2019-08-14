'''GeeksForGeeks
Arrange given numbers to form the biggest number | Set 1
Given an array of numbers, arrange them in a way that yields 
the largest value. For example, if the given numbers are {54, 546, 548, 60}, 
the arrangement 6054854654 gives the largest value. And if the given numbers 
are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.
'''
def bigNumber(A):
    A = sorted([str(x) for x in A])[::-1]
    print(A)
    big = A[0]
    for i in range(1, len(A)):
        if big + A[i] < A[i] + big:
            big = A[i]+big
        else:
            big = big+A[i]
    return big
if __name__ == "__main__":
    # A = [1, 34, 3, 98, 9, 76, 45, 4]
    A = [54, 546, 548, 60]
    # A = [ 3, 30, 34, 5, 9 ]
    print(bigNumber(A))