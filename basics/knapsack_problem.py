'''Knapsack Problem
0-1 Knapsack Problem | DP-10
Given weights and values of n items, put these items in a knapsack of 
capacity W to get the maximum total value in the knapsack. In other words, 
given two integer arrays val[0..n-1] and wt[0..n-1] which represent values 
and weights associated with n items respectively. Also given an integer W which 
represents knapsack capacity, find out the maximum value subset of val[] 
such that sum of the weights of this subset is smaller than or equal to W. 
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
'''
def Knapsack(weight, profit, capacity):
    prof_wt = []
    for i in range(len(weight)):
        prof_wt.append(profit[i]/wight[i])
    