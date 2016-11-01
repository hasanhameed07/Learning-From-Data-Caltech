# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:04:37 2016

@author: hasan
"""
import numpy as np
import math as m
import random

def PLA(X, Y, w, my_g):

    iteration = 0
    n = 1 #learning rate
    misclassified = np.copy(X)
    misclassified_Y = np.copy(Y)
    
    
    def get_misclassified(w):
        points = []
        labels = []
        i = 0
        for x in X:
            g = my_g(w, x)
            if g!=Y[i]:
                points.append(x)
                labels.append(Y[i])
            i += 1
        return [points, labels]
        
    #PLA
    while len(misclassified)>0 and iteration<1000:
        random_index = random.randint(0, len(misclassified)-1)
        random_x = misclassified[random_index]
        random_y = misclassified_Y[random_index]
        g = my_g(w, random_x)
        if g != random_y: 
            w[0] = w[0] + (n*(random_y)*random_x[0])
            w[1] = w[1] + (n*(random_y)*random_x[1])
            w[2] = w[2] + (n*(random_y)*random_x[2])
            [misclassified , misclassified_Y] = get_misclassified(w)
            iteration += 1
        else:
            misclassified = np.delete(misclassified, random_index, 0)
            misclassified_Y = np.delete(misclassified_Y, random_index, 0)


    return iteration
    

# Linear Regression
def LinearRegression(X, Y):
    
    X_m = np.matrix(X)
    Y_m = np.matrix(Y).transpose()
    Xdagger = (X_m.transpose()*X_m).getI()*X_m.transpose()
    w = Xdagger*Y_m
    return np.array(w)


    
def calcGradient(x, y, w):
    x_m = np.matrix(x).transpose()
    w_m = np.matrix(w)
    return np.multiply(-1*y, x_m)/(1. + m.exp(y*(w_m*x_m)))    



def LogisticRegression(X, Y, w):
    N = 100
    ETA = 0.01    
    WTOL = 0.01
    done = False
    epoch = 0
    while not done:
        w_prev = w      
        shuffled_indices = np.random.permutation(N);
        for i in range(N):
            index = shuffled_indices[i];            
            g = calcGradient(X[index], Y[index], w)
            w = w - ETA * g.transpose()
        epoch += 1
        done = np.linalg.norm(w - w_prev) < WTOL;
#    return epoch
    return [np.array(w.ravel().tolist()[0]), epoch]
    

def cross_entropy_error(w, X, Y):
    X = np.matrix(X)
    w_m = np.matrix(w)
    i = 0
    Ein = 0.
    for x_m in X:
        Ein += m.log(1 + m.exp(-1*Y[i]*(w_m*x_m.transpose())))
        i += 1
    return Ein/i