N=input()
sum=0
for i in range(len(N)):
    sum+= int(N[i])*(i+1)
if sum % 11 ==0:
    print("Legal ISBN")
else:
    print("Illegal ISBN")
