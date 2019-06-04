def merge(A, B):
    C = []
    i, j = 0, 0
    M, N = len(A), len(B)
    while M>i and N>j:
        if A[i] < B[j]:
            C.append(A[i])
            i+=1 
        else:
            C.append(B[j])
            j+=1
     
    while M>i:
        C.append(A[i])
        i+=1
    while N>j:
        C.append(B[j])
        j+=1
        
    return C

if __name__ == "__main__":
    A=[[1, 2, 3,5], [1], [1, 6, 7]]
    B=[[2, 4], [0], []]
    for i in range(len(A)):
        print("Input: \nA: %s \nB: %s" %(A[i], B[i]))
        print("Output : %s\n---------------" % merge(A[i], B[i]))
