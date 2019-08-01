'''InterviewBit
Count And Say
Asked in: Facebook
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.
21 is read off as one 2, then one 1 or 1211.
Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.
Example:
if n = 2,
the sequence is 11.'''
def countAndSay(A):
    if A==1:
        return 1
    if A == 2:
        return 11
        
    temp = '11'
    count = 1
    
    for i in range(2, A):
        res = ''
        for j in range(1, len(temp)):
            if temp[j-1] == temp[j]:
                count+=1
            else:
                res += str(count)+temp[j-1]
                count = 1
        res+=str(count)+temp[j]
        temp = res
        # print(int(temp), end=",")
    return temp
print(countAndSay(7))