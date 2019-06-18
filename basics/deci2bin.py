n = int(input())
s=''
while n > 0:
    s+=str(n%2)
    n = n//2
print( s[::-1])
count = 0
result = 0
for i in s:
    if i == '0':3
        count = 0
    else:
        count+=1
    result = max(result, count)
print(result)
decimal = 0
for i in range(result):
    decimal+= (2 **i)
print(decimal)