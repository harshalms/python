class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
	    rows, cols = len(A), len(A[0])
        T, B, L, R = 0, rows-1, 0, cols-1
        dir = 0
        spiral = []
        while T<=B and L<=R:
            if dir ==  0:
                for i in range(L, R+1):
                    spiral.append(A[T][i])
                T+=1
            elif dir == 1:
                for i in range(T, B+1):
                    spiral.append(A[i][R])
                R-=1
            elif dir == 2:
                for i in range(R, L-1, -1):
                    spiral.append(A[B][i])
                B-=1
            else:
                for i in range(B, T-1, -1):
                    spiral.append(A[i][L])
                L+=1
            dir = (dir+1)%4
        return spiral
arr.append(list(map(int, input().rstrip().split())))
obj = Solution()
obj.spiralOrder(arr)