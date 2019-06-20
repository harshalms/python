# Interviewbit, Math section
# Given a column title as appears in an Excel sheet,  return its corresponding column number.
"""
For Ex.
    A -> 1
    
    B -> 2
    
    C -> 3
    
    ...
    
    Z -> 26
    
    AA -> 27
"""
class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        sum = 0
        for i in range(len(A)):
            sum += (ord(A[len(A)-i-1])-ord('A')+1)*(26**i)
        return sum

if __name__ == "__main__":
    A = ["AAA", "AB", "ACC", "BB"]
    obj = Solution()
    for input in A:
        print("Input: %s, Output: %s"% (input, obj.titleToNumber(input)))