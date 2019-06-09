# Enter your code here. Read input from STDIN. Print output to STDOUT
# Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as space-separated strings on a single line (see the Sample below for more detail).
# Note: 0 is considered to be an even index.

def oddEvenSpace(S):
    for i in range(0, len(S), 2):
        print(S[i], end="")
    print(end=" ")
    for i in range(1, len(S), 2):
        print(S[i], end="")
    print()


if __name__== '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        oddEvenSpace(S)

