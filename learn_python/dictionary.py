A = [5, 3, 7, 7, 1, 2, 1, 1]
dicti={}
for i in A:
    if i in dicti:
        dicti[i]+=1
    else:
        dicti[i]=1
for key in dicti: 
    print(dicti[key])