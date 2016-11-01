# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:45:26 2016

@author: culpritz
"""
import numpy as np
import random
#import pandas as pd
#import matplotlib.pyplot as plt

def experiment():
    random.seed()
    X = []
    for x in range(0,100):
        x = [1, random.uniform(-1, 1), random.uniform(-1, 1)]
        X.append(x)
    
    #pd.DataFrame(X, columns=['x0','x', 'y']).plot(kind="scatter", x='x', y='y')
    
    # gen label y
    labels = []    
    w0 = random.random()
    w1 = random.random()
    w2 = random.random()
    for x in X:
        y =  np.sign(w0*1 + w1*x[0] + w2*x[1])
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
    #print w
    
    
    # GRAPH
    
    #[x0, x1, x2] = zip(*X)
    #pd.DataFrame(X, columns=['x0','x', 'y']).plot(kind="scatter", x='x', y='y')
    #plt.scatter(x1, labels)
    #    
    #plt.plot([w.item(1),w.item(2)])
    #plt.show()
    
    def my_g(w, x):
        return np.sign(w.transpose() * x.transpose())
    
    i = 0
    sumError = 0
    for x in X:
        g = my_g(w,x)
        sumError += (g.item(0) != labels[i])
        i += 1
    return sumError/float(i)

avg = 0
for _ in range(0,1000):
    avg += experiment()

print avg/float(1000)    
    