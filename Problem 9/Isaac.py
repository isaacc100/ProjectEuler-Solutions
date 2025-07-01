# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 14:17:45 2025

@author: Isaac
"""
import math

def squareNumbersList(length=10):
    squares = []
    for n in range(1,length):
        squares.append(n**2)
    return squares
if __name__ == "__main__":
    squares = squareNumbersList(1000)
    print("squares found")
    triplets = []
    for a in squares:
        for b in squares:
            for c in squares:
                if (a+b) == c and a >= b:
                    triplets.append([a,b,c])
                    if math.sqrt(a)+math.sqrt(b)+math.sqrt(c) == 1000:
                        print (math.sqrt(a))
                        print (math.sqrt(b))
                        print (math.sqrt(c))
                        print (math.sqrt(a)*math.sqrt(b)*math.sqrt(c))
                        break
