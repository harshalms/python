'''GeeksForGeeks
Arrange given numbers to form the biggest number | Set 1
Given an array of numbers, arrange them in a way that yields 
the largest value. For example, if the given numbers are {54, 546, 548, 60}, 
the arrangement 6054854654 gives the largest value. And if the given numbers 
are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.
'''
def bigNumber(A):
    A = [int(y) for y in sorted([str(x) for x in A])][::-1]
    print(A)
    big = str(A[0])
    for i in range(1, len(A)):
        if int(big+str(A[i])) < int(str(A[i])+big):
            big = str(A[i])+big
        else:
            big = big+str(A[i])
    return int(big)
if __name__ == "__main__":
    A = [1, 34, 3, 98, 9, 76, 45, 4]
    print(bigNumber(A))