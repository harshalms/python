class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        while B>0:
            if A<B:
                A, B = B, A
            A, B = B, A%B
        return A
if __name__ == "__main__":
    obj = Solution()
    input = [(12, 20), (24, 36), (35, 45)]
    for instance in input:
        A, B = instance
        print(obj.gcd(A, B))