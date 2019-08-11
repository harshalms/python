'''InterviewBit
Median of Array
There are two sorted arrays A and B of size m and n respectively.
Find the median of the two sorted arrays 
( The median of the array formed by merging both the arrays ).'''
def findMedianSortedArrays(A, B):
    # i, j, m, n = 0, 0, len(A), len(B)
    # c = []
    # while i<m and j<n:
    #     if A[i]<B[j]:
    #         c.append(A[i])
    #         i+=1
    #     else:
    #         c.append(B[j])
    #         j+=1
    # while i<m and j==n:
    #     c.append(A[i])
    #     i+=1
    # while j<n and i==m:
    #     c.append(B[j])
    #     j+=1
    # if len(c)%2==0:
    #     k = (c[(len(c)//2)-1]+c[len(c)//2])
    #     return k/2
    # else:
    #     return c[len(c)//2]

    if len(B) == 0:
        A, B = B, A
        
    if len(A) == 0:
        if len(B)%2==0:
            return (B[len(B)//2-1]+B(len(B)//2))/2.0
        else:
            return B[len(B)//2]
            
    if len(A)==1 and len(B)==1:
        return (A[0]+B[0])/2.0
        
    midA, midB = 2, 2
    while midA>1 or midB>1:
        midA = (len(A)-1)//2
        midB = (len(B)-1)//2
        if A[midA] > B[midB]:
            A, B = B, A
            A = A[midB:]
            B = B[:midA+1]
            print(A, B)
        else:
            A = A[midA:]
            B = B[:midB+1]
            print("*", A, B)
    c = [min(A[0], B[0]),max(A[0], B[0]), min(A[1], B[1]), max(A[1], B[1])]
    print(c)
    return (c[1]+c[2])/2.0
        
# A = [1, 4, 5]
# B = [2, 3]
# A = [1, 12, 15, 26, 38] 
# B = [2, 13, 17, 30, 45] 
A = [1, 2, 3, 6, 10] 
B = [4, 6, 8, 10, 11]
print(findMedianSortedArrays(A, B))