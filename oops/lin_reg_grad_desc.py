import numpy as np

def gradientDescent(x,y):
    m = len(x)
    t0_curr = t1_curr = 0
    iterations = 10000
    learning_rate = 0.011

    for i in range(iterations):
        yp = t0_curr + t1_curr*x
        
        cost = (1/(2*m))*sum([val**2 for val in (yp-y)])
        t0_d = (1/m)*sum(yp-y)
        t1_d = (1/m)*sum(x*(yp-y))

        t0_curr = t0_curr-learning_rate*t0_d
        t1_curr = t1_curr-learning_rate*t1_d

        print('t0_curr= {}, t1_curr= {}, cost= {}, iterations= {}'.format(t0_curr, t1_curr, cost, i))
    pass


x = np.array([5,6,7,10,12,15,18,20])
y = np.array([7.4,9.3,10.6,15.4,18.1,22.2,24.1,24.8])

# x = np.array([1,2,3,4,5])
# y = np.array([5,7,9,11,13])
gradientDescent(x,y)