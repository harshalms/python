# A=[1,3,5]
# B=[2,4]
# #not required
# C=[]
# # no need to pass as C empty Array, you can define inside function
def merge(A,B):
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

    def divide(A, start, end):
        k, l = [], []
        mid = (start+end)//2
        if end-start>1:
            k=divide(A, start, mid+1)
            l=divide(A, mid, end)
        if end-start<=1:
            merge(k, l)
        return merge(k, l)
if __name__ == "__main__":
    A = [43, 32, 22, 78, 63, 57, 91, 13]
    start = 0, end = len(A)
    print(divide(A,start,end))


