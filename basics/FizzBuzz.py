class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        for i in range(1, A+1):
            if i%15==0:
                print('FizzBuzz', end=" ")
            elif i%3==0 and i%5!=0:
                print('Fizz', end=" ")
            elif i%3!=0 and i%5==0:
                print('Buzz', end=" ")
            else:
                print(i, end=" ")
        print()
if __name__ == "__main__":
    obj = Solution()
    A = 20
    obj.fizzBuzz(A)
