# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 11:07:22 2025

@author: Isaac
"""

#needs to be split into a list
palindromes = []
for x in range(100,1000):
    for y in range(100,1000):
        digits = list(str(x*y))
        if digits == digits[::-1]:
            palindromes.append([x*y,x,y])
palindromes.sort()
print(palindromes)