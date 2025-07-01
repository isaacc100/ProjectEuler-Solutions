# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 10:18:33 2025

@author: Isaac
"""

def fNumbers(max=1000):
    numbers = [1,2,3]
    for n in range(3,max+1):
        if numbers[n-1] <= 4000000:
            numbers.append(numbers[n-2]+numbers[n-1])
        else:
            numbers.pop()
            break
    return numbers
    print(numbers)
def main():
    numbers = fNumbers()
    print (numbers)
    total = 0
    for i in numbers:
        if (i%2)==0:
            total += i
    print (total)
if __name__ == "__main__":
    main()
