A=[1,3,5]
B=[2,4]
#not required
C=[]
# no need to pass as C empty Array, you can define inside function
def merge(A,B,C):
    C = []
    i, j = 0, 0
    M, N = len(A), len(B)
    #while (len(A)>0 and len(B) >0):
     while M>i and N>j:
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
            # instead of removing use pointers, removing element from array taking one more extra operation 
            # which consuming extra time for each element
            #A.remove(A[0])
        else:
            C.append(B[j])
            j+=1
            #B.remove(B[0])
     
    #here only one while gets excuted because, jo bhi chota Array hai (A or B) uper k while me khtm ho rha hai.
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
