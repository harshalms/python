A = [1, 2, 3, 5, 7, 9]
x = 17
def pair(A, x):
    num={}
    for i in A:
        num[i] = i
        if x-i in num:
            return True
    return False
print(pair(A, x))