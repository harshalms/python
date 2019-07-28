'''Interview-Bit
First Missing Integer
Asked in: Model N, InMobi, Amazon
Given an unsorted integer array, find the first missing positive integer.
Example:
Given [1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1
Your algorithm should run in O(n) time and use constant space.'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        s = {}
        for i in A:
            s[i] = i
        for i in range(1, len(A)+1):
            if i not in s:
                return i
        return i+1
a = Solution()
Arr = [[1,2,0], [3,4,-1,1], [-8, -7, -6]]
for A in Arr:
    print(A, "\noutput:", a.firstMissingPositive(A), "\n")
