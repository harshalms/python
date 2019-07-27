'''InterviewBit
Pascal Triangle
Asked in: Google, Amazon
Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
Example:
Given numRows = 5,
Return
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
'''

def pascalTriangle(N):
    import math
    for i in range(N):
        for j in range(i+1):
            x = math.factorial(i)//(math.factorial(i-j) * math.factorial(j))
            print(x, end=" ")
        print()

pascalTriangle(4)