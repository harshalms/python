'''GeeksForGeeks
Minimum swaps required to bring all elements less than or equal to k together
Given an array of n positive integers and a number k. 
Find the minimum number of swaps required to bring 
all the numbers less than or equal to k together.
'''
def minSWAP(A, k):
    count, les, tot = 0, 0, 0
    for i in range(len(A)):
        if A[i] <= k:
            count+=1
        if A[i] > k:
            les = 0
        else:
            les+=1
        tot = max(tot, les)
    return count-tot

A = [2, 1, 5, 6, 3]
# A = [2, 7, 9, 5, 8, 7, 4]
k = 8
print(minSWAP(A, k))