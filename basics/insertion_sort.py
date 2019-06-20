# INSERTION SORT
def insertion_sort(A):
    s=[]
    s.insert(0, A[0])
    for i in range(1, len(A)):
        flag = False
        for j in range(i):
            if A[i] < s[j]:
                s.insert(j, A[i])
                flag = True
                break
        if not flag:
            s.append(A[i])
            # if A[i]>s[j]:
            #     pos = i
    return s


def insertion(A):
    N = len(A)
    for i in range(N):
        
        

if __name__ == "__main__":
    A = [74, 32, 32, 58, 64, 21, 64]
    # A = [1, 2, 3, 4, 5]
    print(insertion_sort(A))
