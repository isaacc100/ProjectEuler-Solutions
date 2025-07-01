# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 16:42:25 2025

@author: Isaac
"""
import time
start = time.perf_counter()

def primes(upto = 1000000):
    primeNumbers = [upto]
    amount = 0
    for n in range(2,upto+1):
        for i in primeNumbers:
                if i >= n:
                    primeNumbers.append(n)
                    primeNumbers.sort()
                    amount += 1
                    if (amount%10000) == 0: print(amount,n)
                    break
                elif (n%i) == 0:
                    break
    primeNumbers.pop()
    return primeNumbers

print(sum(primes(2000000)))
end = time.perf_counter()
print(end-start)
