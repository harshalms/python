class Person:
    def __init__(self, name):
        self.name = name

# class Bricks:
N = int(input("Enter Total Brickswa "))



def is_empty(N, t):
    if N - t <= 0:
        return True
    return False

def who_is_culprit(N):
    patlu_b = 0
    motu_b = 1
    while N:
        patlu_b+=1
        if not is_empty(N, patlu_b):
            N = N - patlu_b
        else:
            return 'Patlu'
        motu_b = patlu_b*2
        if not is_empty(N, motu_b):
            N = N - motu_b
        else:
            return 'motu'
print(who_is_culprit(N))