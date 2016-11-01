# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:45:26 2016

@author: culpritz
"""
import numpy as np
import random
import math
#import pandas as pd
#import matplotlib.pyplot as plt

def experiment():
    random.seed()
    X = []
    for x in range(0,2):
        x = [random.uniform(-1, 1)]
        X.append(x)
    
    #pd.DataFrame(X, columns=['x0','x', 'y']).plot(kind="scatter", x='x', y='y')
    
    # gen label y
    labels = []    
    for x in X:
        y =  math.sin(math.pi*x[0])
    #    print x, y
        labels.append(y)
        
    #w = [0,0,0]
    #for x in X:
    #    h = np.sign(w0*1 + w1*x[0] + w2*x[1])
    X = np.matrix(X)
    Y = np.matrix(labels).transpose()
    Xdagger = (X.transpose()*X).getI()*X.transpose()
    w = Xdagger*Y
    #h = w.transpose()*X
    return w.item(0)
    
    
    # GRAPH
    
    #[x0, x1, x2] = zip(*X)
    #pd.DataFrame(X, columns=['x0','x', 'y']).plot(kind="scatter", x='x', y='y')
    #plt.scatter(x1, labels)
    #    
    #plt.plot([w.item(1),w.item(2)])
    #plt.show()
    
    def my_g(w, x):
        return (w.transpose() * x.transpose())    
    def mean_g(w, x):
        return (np.matrix([1.43755157824]) * x.transpose())
    
    i = 0
    sumError = 0
    for x in X:
        g = my_g(w,x)
        # for variance        
        sumError += (g.item(0) - mean_g(w,x).item(0))**2
        # for Bias
#        sumError += (mean_g.item(0) - labels[i])**2

        i += 1
    return sumError/float(i)

avg = 0
for _ in range(0,10000):
    avg += experiment()
print 'Variance:'
print avg/float(10000)    
    