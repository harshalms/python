import math
N, Q = input().split(" ")
arr=[int(x) for x in input().split(" ")]
for i in range(int(Q)):
    L, R = input().split(" ")
    a=(sum(arr[int(L):int(R)])/(int(R)-int(L)))
    print(math.floor(a))