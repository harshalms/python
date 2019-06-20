A='abcde'

def reverse(s, start):
   if len(s)<=start:
       return None
   reverse(s, start+1)
   print(s[start], end='')

reverse(A, 0)