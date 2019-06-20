N=int(input("Number of Hours? "))
# SH, SM = input().split(" ")
# EH, EM = input().split(" ")

def duration(t):
    h=t//60
    m = t % 60
    print(h, m)

for i in range(N):
    SH, SM = input().split(" ")
    EH, EM = input().split(" ")
    t=abs(int(SH)*60+int(SM)-(int(EH)*60+int(EM)))
    # print(t)
    duration(t)

