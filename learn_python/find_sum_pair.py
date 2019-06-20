A=[5,3,7,9,1,4]
x=10
# def sum(A, x):
#     for i in range(len(A)):
#         for j in range(len(A)):
#             if i!=j:
#                 if(A[i] + A[j] == x):
#                     return True
                
#     return False
# def sum1(A, x):
#     A.sort()
#     i, j = 0, len(A)-1
#     while i<j :
#         if A[i]+A[j]>x:
#             j=j-1
#         elif A[i]+A[j]<x:
#             i=i+1
#         else:
#             return True

def sum2(A, x):
    berij={}
    for val in A:
        if val in berij:
            berij[val]+=1
        else:
            berij[val]=1

    for key in berij:    
        if key==x/2 and berij[key]==1:
            return False
        if x-key in berij:
            return True

        

TEST = [
    [1, 2, 4, 6], # Yes
    [3, 3, 3], # No
    [1, 3, 7], # Yes
    [6, 7], # No
    [5], # No
    [5, 5], # Yes
    [5, 6] # No
]

for A in TEST:
    print(A)
    if sum2(A, x):
        print("Yes")
    else:
        print("No")