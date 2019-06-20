A=sorted(list(input()))
A="".join(A)
B=sorted(list(input()))
B="".join(B)
def anagram(p, q):
    if p!=q:
        return False
    else:
        return True
if anagram(A, B):
    print("Yes, it's an Anagram")
else:
    print("No, It's not an Anagram")