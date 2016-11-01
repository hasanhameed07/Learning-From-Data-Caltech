# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 00:33:13 2016

@author: culpritz
"""
import math as m

def partiald1(u, v):
    return 2*(m.exp(v) + 2*v*m.exp(-1*u))*(u*m.exp(v) - 2*v*m.exp(-1*u))
    
def partiald2(u, v):
    return 2*(u*m.exp(v) - 2*v*m.exp(-1*u))*(u*m.exp(v) - 2*m.exp(-1*u))
    
def evaluate(u, v):
    return (u*m.exp(v)-2*v*m.exp(-1*u))**2

u = 1.
v = 1.
i = 0
E = 1.
print  evaluate(u, v)
#while E >=  m.pow(10, -14):
#    prev_u = u
#    prev_v = v
#    u = prev_u - (0.1)*partiald1(prev_u, prev_v)
#    
#    v = prev_v - (0.1)*partiald2(prev_u, prev_v)
#    
#    E = evaluate(u, v)
#    i = i+1

for i in range(15):
    prev_u = u
    prev_v = v
    u = prev_u - (0.1)*partiald1(prev_u, prev_v)
    
    v = prev_v - (0.1)*partiald2(u, prev_v)
    
    E = evaluate(u, v)
    i = i+1

print E
print i