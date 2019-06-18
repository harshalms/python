#!/bin/python3
# Day 10: Binary Numbers (HackerRank)
# Task 
# Given a base-10 integer,n, convert it to binary (base-2). 
# Then find and print the base-10 integer denoting the maximum 
# number of consecutive 1's in n's binary representation.
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input())
    s=''
    while n > 0 :
        s+=str(n%2)
        n//=2
    count, result = 0, 0
    for i in s:
        if i == '0':
            count = 0
        else:
            count+=1
        result = max(result, count)
    print(result)