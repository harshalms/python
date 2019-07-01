'''GeeksForGeeks
Rearrange an array in order – smallest, largest, 2nd smallest, 2nd largest, ..
Given an array of integers, task is to print the array in the order – 
smallest number, Largest number, 2nd smallest number, 2nd largest number, 
3rd smallest number, 3rd largest number and so on…..
Examples:

Input : arr[] = [5, 8, 1, 4, 2, 9, 3, 7, 6]
Output :arr[] = {1, 9, 2, 8, 3, 7, 4, 6, 5}

Input : arr[] = [1, 2, 3, 4]
Output :arr[] = {1, 4, 2, 3}
The sorting used(O(n^2)) can be improved further using merge sort(O(nlogn)).
'''
def sortNpattern(A):
    tempArr = []
    for i in range(len(A)):
        for j in range(i):
            if A[j]>=A[i]:
                A[i], A[j] = A[j], A[i]
    i, j = 0, len(A)-1
    while i<=j:
        if i==j:
            tempArr.append(A[i])
        else:
            tempArr.append(A[i])
            tempArr.append(A[j])
        i+=1
        j-=1
    A = tempArr
    return A
A = [5, 8, 1, 4, 2, 9, 3, 7, 6]
print(sortNpattern(A))