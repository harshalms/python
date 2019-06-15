# Check for balanced parentheses in an expression
S=input()
def bracket(A):
    count1,count2=0,0
    flag = False
    print(A)
    for i in A:
        if i=='(':
            count1+=1
        if i==')':
            count2+=1
        if count2 > count1:
            flag = True

    if count1==count2 and flag:
        return True
    else:
        return False

print(bracket(S))
