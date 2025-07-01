# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 11:45:33 2025

@author: Isaac
"""

def sumOfSquareNN(to=10):
    value = 0
    for n in range(1,to+1):
        value +=(n**2)
    return value
        
def sumOfNNSquared(to=10):
    value = 0
    for n in range(1, to+1):
        value += n
    return value**2
print(sumOfNNSquared(100)-sumOfSquareNN(100))
