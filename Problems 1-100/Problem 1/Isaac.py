# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 10:08:59 2025

@author: Isaac
"""

def main(i=1000):
    total = 0
    for n in range(1,i+1):
        if n%3 == 0:
            total += n
        elif n%5 == 0:
            total += n
    return total
if __name__ == "__main__":
    print(main(999))