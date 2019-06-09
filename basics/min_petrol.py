# Code Monk
# Monk loves to travel. Since his summer vacation was nearing, he decided to plan a journey to Coderland. Now as Monk is just a competitive programmer, he is always short of money. In order to make this journey happen, he wants to minimize the total travel expenditure.

# Journey to Coderland will be through N checkpoints. Checkpoints are numbered from 0 to . At the start of the journey Monk is present at the checkpoint 0. Also checkpoint  will lead to Coderland. Each checkpoint has a petrol pump which can be used to fill petrol in the car. Now cost of petrol per litre at different checkpoints is given by array C which has 0-based indexing where  is the cost per litre of petrol at the  checkpoint. Note that there is an infinite amount of supply at each checkpoint and car tank is also of infinite capacity. Now another array L is given which has 0-based indexing where  denotes the amount of petrol in litres required to reach the  checkpoint from the  checkpoint. Note that the extra petrol remaining in the tank does not vanishes after reaching a checkpoint. Also, Monk should have atleast  litres of petrol at each checkpoint in order to reach the next checkpoint.

# Can you help Monk estimate the minimum cost required in order complete the journey?

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
