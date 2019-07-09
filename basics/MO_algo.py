'''GeeksForGeeks
MO’s Algorithm (Query Square Root Decomposition) | Set 1 (Introduction)
Let us consider the following problem to understand MO’s Algorithm.
We are given an array and a set of query ranges, we are required to find the 
sum of every query range.
Example:
Input:  arr[]   = {1, 1, 2, 1, 3, 4, 5, 2, 8};
        query[] = [0, 4], [1, 3] [2, 4]
Output: Sum of arr[] elements in range [0, 4] is 8
        Sum of arr[] elements in range [1, 3] is 4  
        Sum of arr[] elements in range [2, 4] is 6
'''
def MO_algorithm(A, query):
    sum = 0
    for i in range(query[0], query[1]+1):
        sum+=A[i]
    return sum
if __name__ == "__main__":
    T = int(input())
    A = [1, 1, 2, 1, 3, 4, 5, 2, 8]
    for i in range(T):
        query = [int(x) for x in input().split()]
        print("Sum of arr[] elements: ",MO_algorithm(A, query))
