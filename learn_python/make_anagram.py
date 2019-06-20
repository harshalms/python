A=input()
B=input()
# A=list(input())
# A=""join(A)
# B=list(input())
# B=""join(B)
dictA={}
dictB={}
def makeAnagram(p,q):
    for i in p:
        if i in dictA:
            countA+=1
        else:
            countA=1
        dictA[i] = countA
    for i in q:
        if i in dictB:
            countB+=1
        else:
            countB=1
        dictB[i] = countB
    count=0
    for key in dictA:
        if key in dictB :
            count+=min(dictA[key],dictB[key])
    return len(p) + len(q) - 2*count


print(makeAnagram(A, B))