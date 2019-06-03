iA=[1,3,5]
B=[2,4]
C=[]

def merge(A,B,C):
    c = []
    i, j = 0, 0
    M, N = len(A), len(B)
    #while (len(A)>0 and len(B) >0):
     while M>i and N>j:
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
            #A.remove(A[0])
        else:
            C.append(B[j])
            j+=1
            #B.remove(B[0])
    
    while M>i:
        C.append(A[i])
        i+=1
    while N>j:
        C.append(B[j])
        j+=1
        
    #if len(A)==0:
    #    for i in range(len(B)):
    #        C.append(B[i])
    #else:
    #    for i in range(len(A)):
    #        C.append(A[i])
    return C

print(merge(A,B,C))
