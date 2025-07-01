# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 10:48:03 2025

@author: Isaac
"""

def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]
primes = sieve(13195) #it worked how lucky
primes[::-1]
for n in primes:
    if (600851475143 % n) == 0:
        print (n)
        