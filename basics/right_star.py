rows=int(input())
# cols=int(input())
for i in range(1, rows+1):
    for j in range(1, i+1):
        print('*', end="")
    print()

print()

# inverted right triangle
for i in range(rows,0,-1):
    for j in range(i):
        print('*', end="")
    print()


for i in range(1, rows+1):
    for j in range(1, rows+1):
        if i+j>=rows+1 and i+j<=2*rows:
            print('*', end="")
        else:
            print(end=" ")
    print()

print()