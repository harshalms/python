def min_cost(N, C, L):
    m, cost = C[0], 0
    for i in range(N):
        m = min(m, C[i])
        cost += m*L[i]
    return cost
    
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        C = list(map(int, input().split()))
        L = list(map(int, input().split()))
        print(min_cost(N, C, L))