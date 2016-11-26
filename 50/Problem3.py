# -*- coding:utf-8 -*-
import math
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
n = 600851475143


def isPrime(n):

    if n == 1:
        return False
    elif n < 4:
        return True
    else:
        r = int(math.floor(math.sqrt(n)))
        for i in range(2,r+1):
            if n % i == 0:
                return False
    return True


def getPrimeFactors(n):
    a = []
    r = int(math.floor(math.sqrt(n)))
    for i in range(2, r+1):
        if n % i == 0 and isPrime(i):
            a.append(i)
    return a

a = getPrimeFactors(n)
print(max(a))
