# -*- coding:utf-8 -*-
import utils.prime

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

p = []

a = 2
while len(p) < 10001:
    if utils.prime.is_prime(a):
        p.append(a)
    a += 1

print p[10000]