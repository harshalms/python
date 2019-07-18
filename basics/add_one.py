"""InterviewBit
Add One To Number
Asked in:  
Google
Microsoft
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124."""
def incrementOne(A):
    A = [str(x) for x in A]
    A = str(int("".join(A)) + 1)
    return [int(x) for x in A]
if __name__ == "__main__":
    A = [[1, 2, 3], [1, 2, 4], [9, 9, 9]]
    for i in range(len(A)):
        print(incrementOne(A[i]))