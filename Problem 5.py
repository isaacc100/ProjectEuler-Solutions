# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 11:22:00 2025

@author: Isaac
"""
def evenlyDivisible(number,by=20):
    for n in range (1,by+1):
        if (number%n) != 0:
            break
        elif n == by:
            return True
def main():
    number = 1
    while True:
        if evenlyDivisible(number,20) == True:
            print(number)
            break
        else:
            if (number%2000000) == 0:
                print(number)
            number += 1
            
main()