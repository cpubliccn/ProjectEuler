# -*- coding:utf-8 -*-

def get_proper_divisors(n):
	a = []
	for i in range(1, int(math.floor(math.sqrt(n)))+1):
		if n % i == 0:
			a.append(i)
			if n/i != i and i != 1:
				a.append(n/i)				
	return a