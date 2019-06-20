name = input("Enter any Name\n")

n = len(name)
for i in range(n):
    if name[i] == name[i].lower():
        print(name[i].upper(), end ="")
    else:
        print(name[i].lower(),end="")