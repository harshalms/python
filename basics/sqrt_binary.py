'''InterviewBit
Square Root of Integer
Asked in: Facebook, Amazon, Microsoft

Implement int sqrt(int x).
Compute and return the square root of x.
If x is not a perfect square, return floor(sqrt(x))
Example :
Input : 11
Output : 3
DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY'''
def sqrt(A):
    # k = int((A**0.5))
    # return k
    start, end = 0, A
    while start<=end:
        mid = (start+end)//2
        if mid*mid==A:
            return mid
        else:
            if mid*mid > A:
                end = mid-1
            else:
                start = mid+1
    return end

if __name__ == "__main__":
    A = [11, 17, 23875, 1297, 625]
    for i in range(len(A)):
        print(A[i], "-->", sqrt(A[i]))