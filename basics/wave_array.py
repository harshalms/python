'''InterviewBit/GeeksForGeeks
Wave Array
Asked in: Google, Adobe, Amazon
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
Example:
Given [1, 2, 3, 4]
One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
NOTE : If there are multiple answers possible, return the one thats lexicographically smallest. 
So, in example case, you will return [2, 1, 4, 3]'''
def wave(A):
    A.sort()
    for i in range(0, len(A)-1, 2):
        A[i], A[i+1] = A[i+1], A[i]
    return A

if __name__ == "__main__":
    A = [[1, 2, 3, 4], [10, 5, 6, 3, 2, 20, 100, 80], [20, 10, 8, 6, 4, 2], [2, 4, 6, 8, 10, 20], 
    [3, 6, 5, 10, 7, 20]]
    
    for i in range(len(A)):
        print(wave(A[i]))