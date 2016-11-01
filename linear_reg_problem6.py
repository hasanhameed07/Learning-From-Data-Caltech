# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:45:26 2016

@author: culpritz
"""
import numpy as np
import random
#import pandas as pd
import matplotlib.pyplot as plt

def experiment():
    random.seed()
    X = []
    for x in range(100):
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
    
    random.seed()
    newX = []
    for x in range(1000):
        x = [1, random.uniform(-1, 1), random.uniform(-1, 1)]
        newX.append(x)
    newLabels = []    
    for x in newX:
        y =  np.sign(w0*1 + w1*x[0] + w2*x[1])
    #    print x, y
        newLabels.append(y)
    newX = np.matrix(newX)
    
    i = 0
    sumError = 0
    for x in newX:
        g = my_g(w,x)
        sumError += (g.item(0) != newLabels[i])
        i += 1
        
    newX = np.array(newX)
    line = np.linspace(-1, 1, 1001) # points from 0-1000
    plt.plot(line, line * w1 + w0, label="f(x)") # makes f(x) line
#    plt.plot(line, line * weights_gx[1]+  weights_gx[0], label="g(x)") # makes g(x) line
    plt.ylim(-1, 1)
    plt.xlim(-1, 1)
    plt.scatter(newX[:, 0][newLabels==1], newX[:, 1][newLabels==1], marker="o", c=("r"), label="+")
    plt.scatter(newX[:, 0][newLabels==-1], newX[:, 1][newLabels==-1], marker="o", c=("b"), label="-")# colored based on Y = +1 or -1
    plt.legend(loc="best")
    
        
    return sumError/float(i)

avg = 0
for _ in range(1):
    avg += experiment()

print avg/float(1)    
    