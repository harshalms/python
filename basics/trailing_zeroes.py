A = 5191
c1, c2 = 0, 0
def trailingZeroes(A):
    c1, c2 = 0, 0
    # for i in range(2, A+1, 2):
    #     while i>0:
    #         if i%2 == 0:
    #             c1+=1
    #             i//=2
    #         else:
    #             break
    for i in range(5, A+1, 5):        
        while i>0:
            if i%5 == 0:
                c2+=1
                i//=5
            else:
                break
    return c2
    # return min(c1, c2)
# print(c1, c2, min(c1, c2))
print(trailingZeroes(A))