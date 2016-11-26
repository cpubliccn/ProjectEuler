# -*- coding:utf-8 -*-
import math


def is_prime(n):
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


def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


def filterout(L1, L2):
    """ inplace substraction of two lists"""
    for i in L1:
        if i in L2:
            L2.remove(i)


def primeGen(n):
    """
    After the first 5 primes the next prime number is the sum of  the last 2
    minus the three prime numbers back
    if it is not a prime number we go for the next one

    """
    primes = [2, 3, 5, 7, 11]
    if n in xrange(1, len(primes) + 1):
        return primes[:n]
    else:
        banlist = []
        count = 6
        while count <= n:
            Next = (primes[-2] + primes[-1]) - primes[-3]
            if not is_prime(Next):
                count -= 1
                banlist.append(Next)
            count += 1
            primes.append(Next)
        filterout(banlist, primes)
        return primes


def get_prime_factors(n):
    a = []
    r = int(math.floor(math.sqrt(n)))
    for i in range(2, r+1):
        if n % i == 0 and is_prime(i):
            a.append(i)
    return a


def get_all_prime_factors(n, a):
    if is_prime(n):
        a.append(n)
    else:
        r = int(math.floor(math.sqrt(n)))
        for i in range(2, r+1):
            if n % i == 0 and is_prime(i):
                a.append(i)
                get_all_prime_factors(n/i, a)
                break


def gcd(m, n):
    a,b = m,n
    c = a % b
    if c == 0:
        return b
    else :
        while c != 0:
            a = b
            b = c
            c = a % b
        return a
