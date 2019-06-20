d=int(input("Number of days? "))
count=0
for i in range(d):
    r, x =input().split(" ")
    c=2*22*int(r)/7
    t= int(x)*100
    if  t<=c :
        count+=1

print(count)