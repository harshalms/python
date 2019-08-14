'''Knapsack Problem'''
def Knapsack(weight, profit, capacity):
    prof_wt = []
    for i in range(len(weight)):
        prof_wt.append(profit[i]/wight[i])
    