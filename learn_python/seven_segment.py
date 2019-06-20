num={'1':2, '2':5, '3':5 ,'4':4 ,'5':5 ,'6':6, '7':3, '8':7, '9':6, '0':6}
T=int(input())
for i in range(0,T):
    sum=0
    N=input()
    for key in N:
        sum+=num[key]
    if sum%2==0:
        print(int((sum//2)*'1'))
    else:
        sum=sum-3
        if sum==0:
            print(7)
        else:
            print(int('7'+(sum//2)*'1'))