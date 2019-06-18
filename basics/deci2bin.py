# n = 8
n = int(input())
# c=[]
s=''
while n > 0:
    # c.append(n%2)
    s+=str(n%2)
    n = n//2
print( s[::-1])
# j = len(c)-1
# print(j)
# while j > -1:
#     print(c[j], end="")
#     j-=1
# print()
