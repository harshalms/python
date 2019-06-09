# Anagrams
# Given two strings, a and b , that may or may not be of the same length,
# determine the minimum number of character deletions required to make a and b anagrams. 
# Any characters can be deleted from either of the strings.
def check_anagram(A, B):
    dictA={}
    dictB={}
    for i in A:
        if i in dictA:
            dictA[i]+=1
        else:
            dictA[i]=1
    for i in B:
        if i in dictB:
            dictB[i]+=1
        else:
            dictB[i]=1
    count=0
    for key in dictA:
        if key in dictB :
            count+=min(dictA[key],dictB[key])
    return (len(A) + len(B) - 2*count)


T = int(input()) # Number of test cases

for i in range(T):
    A = input()
    B = input()
    print(check_anagram(A, B))