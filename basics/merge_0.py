A=[1,3,5]
B=[2,4]
C=[]

def merge(A,B,C):
    while (len(A)>0 and len(B) >0):
        if A[0] < B[0]:
            C.append(A[0])
            A.remove(A[0])
        else:
            C.append(B[0])
            B.remove(B[0])

    if len(A)==0:
        for i in range(len(B)):
            C.append(B[i])
    else:
        for i in range(len(A)):
            C.append(A[i])
    return C

print(merge(A,B,C))
