'''GeeksForGeeks
Arrange given numbers to form the biggest number | Set 1
Given an array of numbers, arrange them in a way that yields 
the largest value. For example, if the given numbers are {54, 546, 548, 60}, 
the arrangement 6054854654 gives the largest value. And if the given numbers 
are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.
'''
def bigNumber(A):
    for i in range(len(A)):
        a = str(A[i])
        A[i] = [int(a[0]), A[i]]
    A.sort()        
    A = A[::-1]
    # print(A)
    big = str(A[0][1])
    for i in range(1, len(A)):
        if int(big+str(A[i][1])) < int(str(A[i][1])+big):
            big = str(A[i][1])+big
        else:
            big = big+str(A[i][1])
    return int(big)
if __name__ == "__main__":
    A = [1, 34, 3, 98, 9, 76, 45, 4]
    print(bigNumber(A))