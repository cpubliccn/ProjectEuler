# -*- coding:utf-8 -*-
import utils.prime
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

limit = 2000000

#primes = [x for x in range(1, limit+1) if utils.prime.is_prime(x)]
#print sum(primes)

primes = [x for x in utils.prime.primes_sieve(limit)]
print sum(primes)
