s1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s2='0123456789'
s3='abcdefghijklmnopqrstuvwxyz'
s=input("Enter Messege? ")
k=int(input())
for i in range(len(s)):
    if s[i] in s1:
        print(s1[(s1.index(s[i])+k)%len(s1)], end="")
    elif s[i] in s3:
        print(s3[(s3.index(s[i])+k)%len(s3)], end="")
    elif s[i] in s2:
        print(s2[(s2.index(s[i])+k)%len(s2)], end="")
    else:
        print(s[i], end="")
