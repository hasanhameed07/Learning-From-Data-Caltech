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

def experiment(N):
    random.seed()
    X = []
    for x in range(N):
        x = [1., random.uniform(-1, 1), random.uniform(-1, 1)]
        X.append(x)
    X = np.array(X)
    
    # gen label y
    Y = [] 
    x1 = X[random.randint(0,len(X)-1)]
    x2 = X[random.randint(0,len(X)-1)]
    [w0, w1, w2] = [ (x2[2] - x1[2])*x1[1] - (x2[1]-x1[1])*x1[2], -(x2[2] - x1[2]), x2[1] - x1[1]]
    

    def evalLine(x):   
        y =  np.sign(w0*1 + w1*x[1] + w2*x[2])
        return 1 if y>0 else -1
    
    for x in X:
        Y.append(evalLine(x))
    Y = np.array(Y)
    
#    Graph
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


        
    w = np.array([0.,0.,0.])
    [w, epochs] = algos.LogisticRegression(X, Y, w)
#    return epochs
    
    # GRAPH
    print w0, w1, w2
    print w
    m = -w[1]/w[2]
    c = -w[0]/w[2]
    line = np.linspace(-1, 1, 10)
    y = m*line + c
    plt.plot(line, y, label="g(x)")

    
    # Test Simulation
    def simulation(N):
        random.seed()
        X = []
        for x in range(N):
            x = [1, random.uniform(-1, 1), random.uniform(-1, 1)]
            X.append(x)
        Y = []    
        for x in X:
            y =  evalLine(x)
        #    print x, y
            Y.append(y)   
        X = np.array(X)
        Y = np.array(Y) 
        return [X, Y]
    
    [X, Y] = simulation(N)
        
    # error check
    return algos.cross_entropy_error(w, X, Y)

avg = 0.
N = 100
repeat_experiment_n = 1
for _ in range(repeat_experiment_n):
    avg += experiment(N)

print 'Avg Ein: {0}'.format(avg/repeat_experiment_n)   
    