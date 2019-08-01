'''InterviewBit
Median of Array
There are two sorted arrays A and B of size m and n respectively.
Find the median of the two sorted arrays 
( The median of the array formed by merging both the arrays ).'''
def findMedianSortedArrays(A, B):
        i, j, m, n = 0, 0, len(A), len(B)
        c = []
        while i<m and j<n:
            if A[i]<B[j]:
                c.append(A[i])
                i+=1
            else:
                c.append(B[j])
                j+=1
        while i<m and j==n:
            c.append(A[i])
            i+=1
        while j<n and i==m:
            c.append(B[j])
            j+=1
        if len(c)%2==0:
            k = (c[(len(c)//2)-1]+c[len(c)//2])
            return k/2
        else:
            return c[len(c)//2]
A = [1, 4, 5]
B = [2, 3]
print(findMedianSortedArrays(A, B))