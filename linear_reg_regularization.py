# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:45:26 2016

@author: culpritz
"""
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import algos

def experiment(lambdafactor):
    # Gen sample data

    def transform(x1, x2):        
        return [1, x1, x2, x1**2, x2**2, x1*x2, abs(x1-x2), abs(x1+x2)]

    X = []
    data = np.loadtxt('./in.dta.txt')
    for d in data:
        x1 = d[0]
        x2 = d[1]
        X.append(transform(x1, x2))
    
    Y = data[:, 2] 
    

    w = algos.LinearRegressionRegularized(X, Y, 10**lambdafactor)
    
    
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

    testing_data = np.loadtxt('./out.dta.txt')
    X_test = []
    for d in testing_data:
        x1 = d[0]
        x2 = d[1]
        X_test.append(transform(x1, x2))
    
    # gen Line that passes through 2 random points
    Y_test = testing_data[:, 2] 
    
    
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
    Ein = sumError/float(i)

    i = 0
    sumError = 0
    for x in X_test:
        g = my_g(w,x)
        sumError += int((g != Y_test[i]))
        i += 1
    Eout = sumError/float(i)
    print [lambdafactor, Ein , Eout]
    return 1

N = 1
for _ in np.linspace(-10, 10, 21):
    avg = experiment(_)

print avg
    