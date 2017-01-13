# -*- coding:utf-8 -*-

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def factorial(n):
	result = 1
	for i in range(1, n+1):
		result *= i
	return result


def factorial2(n):
	return reduce(lambda x,y:x*y, range(1, n+1)) 


result = str(factorial2(100))
sum = 0
for i in range(len(result)):
    sum += int(result[i])

print sum