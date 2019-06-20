# n = 10000
# x = 2
# prev = x
# curr = 1
# for i in range(1, n+1):
#     curr = i*prev
#     prev = curr
# print(curr%((10 **6)+3))
import sys
dicti=[[0,32],[0,36],[0,39],[0,40]]
min1, min2 = sys.maxsize, sys.maxsize
for i in range(len(dicti)):
        if min1 > dicti[i][1]:
            min2 = min1
            min1 = dicti[i][1]
            # print("min1----->",min1,min2)
            
        if (dicti[i][1] != min1) and (min2 > dicti[i][1]):
            min2 = dicti[i][1]
            # print("min2----->",min2,min1)
print(min1, min2)