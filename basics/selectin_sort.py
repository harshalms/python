# Selection sort. O(n^2)

def selction_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        

if __name__ == '__main__':
    arr = [74, 64, 89, 21, 21, 64]
    (selction_sort(arr))
    print(arr)