''' HackerRank All Women's Codesprint 2019 >> Alpha and Beta
Our friends Alpha and Beta found a magical treasure of Asgard. It consists of  piles of gold coins. It is magical since if anyone tries to take a pile of  coins, all the other piles of exactly  coins (if they exist) disappear.

Alpha and Beta only have one turn each to choose a pile for themselves starting with Alpha. 
In one turn, a complete pile of gold coins can be chosen and since our friends are smart they 
will choose the pile with the maximum coins.
Find the number of coins Beta will get in his turn.
Function Description:
Complete the alphaBeta function in the editor below. It should return an integer representing the 
number of coins Beta will get in his turn.
alphaBeta has the following parameter(s):
pile: an integer array
Input Format
First line of the input contains a single integer n, number of piles.
Second line of the input contains n space seperated integers, number of gold coins in each pile.

'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alphaBeta' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY pile as parameter.
#

def alphaBeta(pile):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    pile = list(map(int, input().rstrip().split()))

    result = alphaBeta(pile)

    fptr.write(str(result) + '\n')

    fptr.close()
