s=input()
arr=[i for i in s]
def tag(arr):
    if (int(arr[0])+int(arr[1]))%2!=0 or (int(arr[3])+int(arr[4]))%2!=0 or (int(arr[4])+int(arr[5]))%2!=0 or (int(arr[7])+int(arr[8]))%2!=0:
        return False
    elif arr[2]=="A" or "E" or "I" or "O" or "U" or "Y":
        return False
    else:
        True
print(tag(arr))