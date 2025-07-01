# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 12:00:28 2025

@author: Isaac
"""
def primes(output,upto = 1000000):
    primeNumbers = [upto]
    amount = 0
    for n in range(2,upto+1):
        for i in primeNumbers:
                if i >= n:
                    primeNumbers.append(n)
                    primeNumbers.sort()
                    amount += 1
                    if (amount%10000) == 0: print(amount,n)
                    if amount == output:
                        print(n)
                        break
                    break
                elif (n%i) == 0:
                    break
    primeNumbers.pop()
print(primes(10001))