# -*- coding:utf-8 -*-

'''
Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import math

def sum_of_proper_divisors(n):
	return sum(get_proper_divisors(n))


def is_amicable_nubmers(n):
	sum1 = sum_of_proper_divisors(n)
	sum2 = sum_of_proper_divisors(sum1)
	return sum2 == n and n != sum1


def get_proper_divisors(n):
	a = []
	for i in range(1, int(math.floor(math.sqrt(n)))+1):
		if n % i == 0:
			a.append(i)
			if n/i != i and i != 1:
				a.append(n/i)				
	return a


r = []
for n in range(10000):
	if n in r:
		continue
	if is_amicable_nubmers(n):
		r.append(n)
		r.append(sum(get_proper_divisors(n)))

print r, sum(r)