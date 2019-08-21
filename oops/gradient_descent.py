import numpy as np

def gradientDescent(x,y):
    m = len(x)
    learning_rate = 0.04
    t0_curr = t1_curr = 0
    iterations = 1500
    # cost = 5000
    
    for i in range(iterations):
        yp = t0_curr + t1_curr*x

        # prev = cost
        cost = (1/(2*m))*sum([val**2 for val in (y-yp)])
        # curr = cost

        t0_d = -(1/m)*sum(y-yp)
        t1_d = -(1/m)*sum(x*(y-yp))

        t0_curr = t0_curr - learning_rate*t0_d
        t1_curr = t1_curr - learning_rate*t1_d

        print('t0_curr= {}, t1_curr= {}, cost= {}, iterations= {}'.format(t0_curr, t1_curr, cost, i))
        # print(prev, curr)
        # if prev-curr < (10**-12):
        #     break

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradientDescent(x,y)