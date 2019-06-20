import math

def prime(N):
    count, shout = 0, 0
    if N == 1 or N <=0:
            count=1
    if N==2:
        count=0
    for i in range(2, int(math.sqrt(N))+1):
        if N > 2:
            if N % i ==0:
                count+=1  

    j=sum(int(x) for x in str(N))
    if j == 1 or j <=0:
            shout=1
    if j==2:
        shout=0
    for i in range(2, int(math.sqrt(j))+1):
        if j > 2:
            if j % i ==0:
                shout+=1  



    if count==0 and shout==0:
        print(N)
    # else:
    #     print("Prime", N)

if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    for i in range(n, m+1):
        prime(i)