'''GeeksForGeeks
Find k numbers with most occurrences in the given array
Given an array of n numbers and a positive integer k. 
The problem is to find k numbers with most occurrences, i.e., 
the top k numbers having the maximum frequency. If two numbers 
have same frequency then the larger number should be given preference. 
The numbers should be displayed in decreasing order of their frequencies. 
It is assumed that the array consists of k numbers with most occurrences.
Examples:

Input : arr[] = {3, 1, 4, 4, 5, 2, 6, 1}, 
             k = 2
Output : 4 1
Frequency of 4 = 2
Frequency of 1 = 2
These two have the maximum frequency and
4 is larger than 1.

Input : arr[] = {7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9},
            k = 4
Output : 5 11 7 10
'''
def find_frequency(A, k):
    freq, count = {}, 0
    for i in A:
        if i in freq:
            freq[i] +=1
        else:
            count = 1
            freq[i] = count
    A = []
    for key in freq:
        A.append((freq[key], key))
    A.sort()
    for i in range(1, k+1):
        print(A[-i][1], end=" ")
if __name__ == "__main__":
    A = [[3, 1, 4, 4, 5, 2, 6, 1], [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]]
    k = [2, 4]
    for i in range(len(A)):
        print("Following are the numbers with most frequency: ")
        find_frequency(A[i], k[i])
        print()