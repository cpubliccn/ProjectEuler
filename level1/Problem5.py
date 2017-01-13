# -*- coding:utf-8 -*-
import utils.prime

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

r = []

for i in range(2, 21):
    a = []
    utils.prime.get_all_prime_factors(i, a)
    for x in a:
        if x in r:
            r.remove(x)
    r.extend(a)

#print r
x = 1
for i in r:
    x *= i

print x
