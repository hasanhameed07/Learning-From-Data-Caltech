# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:45:26 2016

@author: culpritz
"""
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import algos

def experiment(k):
    # Gen sample data

    def transform(x1, x2):        
        phi = [1, x1, x2, x1**2, x2**2, x1*x2, abs(x1-x2), abs(x1+x2)]
        return phi[0:int(k+1)]        
        
    X = []
    data = np.loadtxt('./in.dta.txt')
    testing, training = data[:25,:], data[25:35,:]
    for d in training:
        x1 = d[0]
        x2 = d[1]
        X.append(transform(x1, x2))
    
    Y = training[:, 2] 
    

    w = algos.LinearRegression(X, Y)
    
    
    def my_g(w, x):
        y = np.sign(w.transpose().dot(np.transpose([x])).item(0))
        return 1 if y==0 else y
    

    # Test

#    problem #1
#    testing_data = testing
    # problem #2
    testing_data = np.loadtxt('./out.dta.txt')
    X_test = []
    for d in testing_data:
        x1 = d[0]
        x2 = d[1]
        X_test.append(transform(x1, x2))
    
    Y_test = testing_data[:, 2] 
    
    # E_in
    i = 0
    sumError = 0
    for x in X:
        g = my_g(w,x)
        sumError += int((g != Y[i]))
        i += 1
    Ein = sumError/float(i)

    # E_out
    i = 0
    sumError = 0
    for x in X_test:
        g = my_g(w,x)
        sumError += int((g != Y_test[i]))
        i += 1
    Eout = sumError/float(i)
    return [k, Ein , Eout]

N = 1
for k in [7]:
    avg = experiment(k)
    print avg
    