# One of the best solutions for checking a number isPrime or not.
A = int(input())
def isPrime(A):
    if A <= 1:
        return 0
    for i in range(2, int(A **0.5)+1):
        if A % i ==0:
            return 0        # 0 implies not a prime number
    return 1                # 1 implies a prime number
print(isPrime(A))