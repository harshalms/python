'''HackerRank
Objective 
Today, we're building on our knowledge of Arrays by adding another dimension. 
Check out the Tutorial tab for learning materials and an instructional video!
Context 
Given a  2D Array, :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
Task 
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
Input Format

There are  lines of input, where each line contains  space-separated integers describing 2D Array ; 
every value in  will be in the inclusive range of  to .
Constraints
Output Format
Print the largest (maximum) hourglass sum found in .
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output
19
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(A):
    
    result = -(2**32)
    for i in range(len(A)-2):
        tot = 0
        for j in range(len(A)-2):
            tot=sum(A[i][j:j+3])+sum(A[i+2][j:j+3])+A[i+1][j+1]
            result = max(tot, result)
    return result

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourglass(arr))
