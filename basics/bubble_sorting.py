'''HackerRank
Day 20: Sorting
Objective 
Today, we're discussing a simple sorting algorithm called Bubble Sort. 
Check out the Tutorial tab for learning materials and an instructional video!
Task 
Given an array,a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. 
Once sorted, print the following 3 lines:
Array is sorted in numSwaps swaps. 
where numSwaps is the number of swaps that took place.
First Element: firstElement 
where firstElement is the first element in the sorted array.
Last Element: lastElement 
where lastElement is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of 
all swaps that occur during execution.
'''
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
def sort(a):
    numSwaps = 0
    for i in range(n-1):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps+=1
    print("Array is sorted in {} swaps.".format(numSwaps))
    print("First element:",a[0])
    print("Last Element:", a[-1])
sort(a)