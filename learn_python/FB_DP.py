L=int(input("standerd size of squared photo? "))
N = int(input("Number of Photos? "))

def profile_pic(H, W, L):
    if W<L or H<L:
        print("UPLOAD ANOTHER")
    elif W>L or H>L:
        print("CROP IT")
    else:
        print("ACCEPTED")

while N>0:
    a, b = input().split()
    tuple = int(a), int(b)
    profile_pic(tuple[0], tuple[1], L)
    N-=1