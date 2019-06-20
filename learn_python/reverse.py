A=[1, 2, 3, 3, 7, 7]
B=[]
for i in range(len(A)):
    B.append(A.pop())
print(B)