import sys
Arr = list(map(int, input().split()))
# print(Arr)
# min1 is minimum value in the input array. 
# min2 is the second minimum in the input array.
min1, min2 = sys.maxsize, sys.maxsize
for i in range(len(Arr)):
        if min1 > Arr[i]:
            min2 = min1
            min1 = Arr[i] 
        if (Arr[i] != min1) and (min2 > Arr[i]):
            min2 = Arr[i]
print(min1, min2)
