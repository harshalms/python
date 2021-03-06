'''GeeksForGeeks
Reorder an array according to given indexes
Given two integer arrays of same size, “arr[]” and “index[]”, 
reorder elements in “arr[]” according to given index array. 
It is not allowed to given array arr’s length.
Example:

Input:  arr[]   = [10, 11, 12];
        index[] = [1, 0, 2];
Output: arr[]   = [11, 10, 12]
        index[] = [0,  1,  2] 

Input:  arr[]   = [50, 40, 70, 60, 90]
        index[] = [3,  0,  4,  1,  2]
Output: arr[]   = [40, 60, 90, 50, 70]
        index[] = [0,  1,  2,  3,   4] 
Expected time complexity O(n) and auxiliary space O(1)
'''
def reorder(arr, index):
    tempArr = [0]*len(arr)
    for i in range(len(arr)):
        tempArr[index[i]] = arr[i]
    arr = tempArr
    return arr
if __name__ == "__main__":
    arr = [[10, 11, 12], [50, 40, 70, 60, 90], [47, 58, 39, 34, 80]]
    index = [[1, 0, 2], [3,  0,  4,  1,  2], [4,  0,  2,  1,   3]]
    for i in range(len(arr)):
        print(reorder(arr[i], index[i]))