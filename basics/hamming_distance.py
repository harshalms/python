"""
Hamming distance between two non-negative integers is defined as the number of 
positions at which the corresponding bits are different.
For example,
HammingDistance(2, 7) = 2, as only the first and the third bit differs in the 
binary representation of 2 (010) and 7 (111).
Given an array of N non-negative integers, find the sum of hamming distances 
of all pairs of integers in the array.
Return the answer modulo 1000000007.
"""

def hammingDistance(a, b):
    s1, s2 = '', ''
    while a>0 or b>0:
        s1+=str(a%2)
        a//=2
        s2+=str(b%2)
        b//=2
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count+=1
    return count
if __name__ == "__main__":
    sum = 0
    A = [ 96, 96, 7, 81, 2, 13 ]
    for i in range(len(A)):
        for j in range(len(A)):
            sum+=(hammingDistance(A[i], A[j]))
    print(sum%1000000007)