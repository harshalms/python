'''GeeksForGeeks
Rearrange positive and negative numbers using inbuilt sort function
Given an array of positive and negative numbers, arrange them such 
that all negative integers appear before all the positive integers 
in the array without using any additional data structure like 
hash table, arrays, etc. The order of appearance should be maintained.
Examples:
Input :  arr[] = [12, 11, -13, -5, 6, -7, 5, -3, -6]
Output : arr[] = [-13, -5, -7, -3, -6, 12, 11, 6, 5]

Input :  arr[] = [-12, 11, 0, -5, 6, -7, 5, -3, -6]
Output : arr[] =  [-12, -5, -7, -3, -6, 11, 0, 6, 5]
'''
def PosNegArrange(A):
    for i in range(len(A)):
        j = i
        while j>0:
            if A[j]<0 and A[j-1]>=0:
                A[j-1], A[j] = A[j], A[j-1]
            j-=1
    return A
if __name__ == "__main__":
    A = [[12, 11, -13, -5, 6, -7, 5, -3, -6], [-12, 11, 0, -5, 6, -7, 5, -3, -6]]
    for i in range(len(A)):
        print(PosNegArrange(A[i]))