directions=input()
position=[0,0]
for i in directions:
    if i=='L':
        position[0]-=1
    elif i=='R':
        position[0]+=1
    elif i=='U':
        position[1]+=1
    else:
        position[1]-=1
print(position[0],position[1])