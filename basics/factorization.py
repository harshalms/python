# Factorization.
# Time complexity: O(sqrt(n))
n = int(input())
factors = [1, n]
for i in range(2, int(n **0.5) + 1):
    if n % i == 0:
        factors.append(i)
        if i != (n **0.5):
            factors.append(n//i)
factors.sort()
for i in factors:
    print(i, end=" ")