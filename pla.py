# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:45:26 2016

@author: culpritz
"""
import numpy as np
import random
#import pandas as pd
import matplotlib.pyplot as plt
import algos

def experiment():
    random.seed()
    X = []
    for x in range(0,10):
        x = [1., random.uniform(-1, 1), random.uniform(-1, 1)]
        X.append(x)
    X = np.array(X)
    #pd.DataFrame(X, columns=['x0','x', 'y']).plot(kind="scatter", x='x', y='y')
    
    # gen label y
    Y = [] 
    x1 = X[random.randint(0,len(X)-1)]
    x2 = X[random.randint(0,len(X)-1)]
    [w0, w1, w2] = [ (x2[2] - x1[2])*x1[1] - (x2[1]-x1[1])*x1[2], -(x2[2] - x1[2]), x2[1] - x1[1]]
    

    def evalLine(x):   
        y =  np.sign(w0*1 + w1*x[1] + w2*x[2])
        return 1 if y==0 else y
    
    for x in X:
    #    print x, y
        Y.append(evalLine(x))
    Y = np.array(Y)
    
    plt.ylim(-1, 1)
    plt.xlim(-1, 1)
    m = -w1/w2
    c = -w0/w2
    line = np.linspace(-1, 1, 10) # points from 0-1000
    y = m*line + c
    plt.plot(line, y, 'r--', label="f(x)") # makes f(x) line
    plt.scatter(X[:, 1][Y==1], X[:, 2][Y==1], marker="o", c=("r"), label="+")
    plt.scatter(X[:, 1][Y==-1], X[:, 2][Y==-1], marker="o", c=("b"), label="-")# colored based on Y = +1 or -1
    plt.legend(loc="best")
    
    
    def my_g(w, x):
        y = np.sign(w.dot(np.transpose([x])))
        return 1 if y[0]==0 else y[0]


        
    w = np.array([0.,0.,0.])
    return algos.PLA(X, Y, w, my_g)
    
    # GRAPH
#    print w0, w1, w2
#    print w
    m = -w[1]/w[2]
    c = -w[0]/w[2]
    line = np.linspace(-1, 1, 10)
    y = m*line + c
    plt.plot(line, y, label="g(x)")

    
    # Test Simulation
    random.seed()
    X = []
    for x in range(100):
        x = [1, random.uniform(-1, 1), random.uniform(-1, 1)]
        X.append(x)
    X = np.array(X)
    Y = []    
    for x in X:
        y =  evalLine(x)
    #    print x, y
        Y.append(y)   
    Y = np.array(Y) 
    
    
    # error check
    i = 0
    Ein = 0.
    for x in X:
        g = my_g(w, x)
        Ein += int(g!=Y[i])
        i += 1
    return Ein/i

avg = 0.
for _ in range(1):
    avg += experiment()

print 'Avg Ein: {0}'.format(avg/1)   
    