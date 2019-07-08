'''GeeksForGeeks
Alternative Sorting
Given an array of integers, print the array in such a way that the first 
element is first maximum and second element is first minimum and so on.

Examples :

Input : arr[] = {7, 1, 2, 3, 4, 5, 6}
Output : 7 1 6 2 5 3 4

Input : arr[] = {1, 6, 9, 4, 3, 7, 8, 2}
Output : 9 1 8 2 7 3 6 4
'''
def alternate_sorting(A):
    A.sort()
    print(A)
    for j in range(0, len(A), 2):
        temp = A[len(A)-1]
        for i in range(len(A)-1, j, -1):
            A[i] = A[i-1]
        A[j] = temp
    return A
if __name__ == "__main__":
    A = [[7, 1, 2, 3, 4, 5, 6], [1, 6, 9, 4, 3, 7, 8, 2]]
    for i in range(len(A)):
        print(alternate_sorting(A[i]))
        print()