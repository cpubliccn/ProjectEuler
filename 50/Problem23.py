# -*- coding:utf-8 -*-

'''
Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means 
that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called 
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
it can be shown that all integers greater than 28123 can be written as the sum of 
two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum of 
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.
'''
import sys,math,itertools
import time

sys.path.append("..")
start = time.time()
import utils.divisors

def get_divisor_type(n):
	sum_of_divisors = sum(utils.divisors.get_proper_divisors(n))
	if sum_of_divisors == n:
		return 0
	elif sum_of_divisors < n:
		return -1
	else:
		return 1


abundant_numbers = []
sum_abundant_nums = []
a = range(1, 28124)

for i in range(1, 28124):
	if get_divisor_type(i) == 1:
		abundant_numbers.append(i)

print "generate abundant_numbers:", len(abundant_numbers), time.time() - start

for i in abundant_numbers:	
	idx = abundant_numbers.index(i)
	for j in abundant_numbers[idx:]:
		k = i+j
		if k < 28124 and k not in sum_abundant_nums:
			sum_abundant_nums.append(i+j)

print "generate sum_abundant_numbers:", len(sum_abundant_nums), time.time() - start
print sum_abundant_nums[0],sum_abundant_nums[-1]

b = [n for n in a if n not in sum_abundant_nums]

result = sum(b)
end = time.time()

print end - start, result
