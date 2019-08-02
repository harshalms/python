'''InterviewBit
Largest Number
Asked in: Amazon, Goldman Sachs, Microsoft
Given a list of non negative integers, arrange them such that they form the largest number.
For example:
Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.'''

def merge(A, B):
    C = []
    i, j = 0, 0
    M, N = len(A), len(B)
    while M>i and N>j:
        if A[i]+B[j] > B[j]+A[i]:
            C.append(A[i])
            i+=1 
        else:
            C.append(B[j])
            j+=1
     
    while M>i:
        C.append(A[i])
        i+=1

    while N>j:
        C.append(B[j])
        j+=1    

    return C

def divide(A, start, end):
        if end-start>1:
            mid = (start+end)//2
            k=divide(A, start, mid)
            l=divide(A, mid, end)
            return merge(k, l)
        if end-start<=1:
            return A[start:end]

if __name__ == "__main__":
    # A = [43, 32, 22, 78, 63, 57, 91, 13]
    # A = [1, 34, 3, 98, 9, 76, 45, 4]
    # A = [54, 546, 548, 60]
    # A = [ 3, 30, 34, 5, 9 ]
    A=[8, 89]
    A = [str(x) for x in A]
    start, end = 0, len(A)
    print("".join(divide(A,start,end)))