s='abcdefghijklmnopqrstuvwxyz'
alpha={}
count=0
# print(len(s))
for i in range(len(s)):
    alpha[s[i]]=count+1
    count+=1
string=input()
sum=0
for i in range(len(string)):
    sum+=alpha[string[i]]
print(sum)
