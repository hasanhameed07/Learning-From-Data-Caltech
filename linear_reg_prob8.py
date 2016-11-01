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
    # Gen sample data

    random.seed()
    X = []
    for x in range(N):
        x = [1, random.uniform(-1, 1), random.uniform(-1, 1)]
        X.append(x)
    X = np.array(X)
    
    # gen Line that passes through 2 random points
    Y = [] 
    
    def evalLine(x):   
        y =  np.sign(x[1]**2 + x[2]**2 - 0.6 )
        return 1 if y==0 else y
            
    # apply target function on sample
    for x in X:
        #    print x, y
        Y.append(evalLine(x))


    w = algos.LinearRegression(X, Y)
    
    
    
    # GRAPH
#    plt.ylim(-1, 1)
#    plt.xlim(-1, 1)
#    m = -w1/w2
#    c = -w0/w2
#    line = np.linspace(-1, 1, 10) # points from 0-1000
#    y = m*line + c
#    plt.plot(line, y, 'r--', label="f(x)") # makes f(x) line
#    plt.scatter(X[:, 1], Y, marker="o", c=("r"), label="+")
##    plt.scatter(X[:, 1][Y<0], X[:, 2][Y<0], marker="o", c=("b"), label="-")# colored based on Y = +1 or -1
#    plt.legend(loc="best")
#    
    
    def my_g(w, x):
        y = np.sign(w.transpose().dot(np.transpose([x])).item(0))
        return 1 if y==0 else y
    

    # Test Simulation
    def simulation(N):
        random.seed()
        X = []
        for x in range(N):
            x = [1, random.uniform(-1, 1), random.uniform(-1, 1)]
            X.append(x)
        X = np.array(X)
        Y = []    
        for x in X:
            y =  evalLine(x)
        #    print x, y
            Y.append(y)   
        Y = np.array(Y) 
        return [X, Y]
    
    
    # GRAPH
#    w = np.array(w)
#    print w0, w1, w2
#    print w
#    m = -w[1]/w[2]
#    c = -w[0]/w[2]
#    line = np.linspace(-1, 1, 10)
#    y = m*line + c
#    plt.plot(line, y, label="g(x)")
    
#    [X, Y] = simulation(1000)
    
    i = 0
    sumError = 0
    for x in X:
        g = my_g(w,x)
        sumError += int((g != Y[i]))
        i += 1

        
    return sumError/float(i)

avg = 0.
N = 1000
for _ in range(N):
    avg += experiment(1000)

print avg/float(N)    
    