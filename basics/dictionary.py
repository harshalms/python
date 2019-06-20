# A = 'ajdfaghfsdasgdfagsdhgasdfasfdahd'
A = 'gsadasfdashdasdkjgadhjdyjhasfdasgd'
# A ='aabccdeffgh'
dictA = {}
for i in A:
    if i in dictA:
        dictA[i]+=1
    else:
        dictA[i] = 1
    # dictA[i] = count
print(dictA)
print(len(A))
tot=0
for i in dictA:
    tot+=dictA[i]
print(tot)