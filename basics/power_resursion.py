'''InterviewBit
Implement Power Function
Asked in: Google, LinkedIn
Implement pow(x, n) % d.
In other words, given x, n and d,
find (x^n % d)
Note that remainders on division cannot be negative. 
In other words, make sure the answer you return is non negative.
Input : x = 2, n = 3, d = 3
Output : 2
2^3 % 3 = 8 % 3 = 2.'''

def power(x, n, d):
    if x==0:
        return 0
    if n==0 and x!=0:
        return 1
    elif n==1:
        return x%d
    elif n == 2:
        return (x*x)%d
    else:
        if n%2==1:
            return (power(x, n//2, d)*power(x, n//2, d)*x)%d
        else:
            return (power(x, n//2, d)*power(x, n//2, d))%d

print(power(2, 3, 3))
print(power(71045970, 41535484, 64735492))
print(power(6, 4))