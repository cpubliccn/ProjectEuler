# -*- coding:utf-8 -*-

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

r = range(1000)
a = [x for x in r if x % 3 == 0]
b = [y for y in r if y % 5 == 0 and y not in a]
sum = sum(a) + sum(b)
print(sum)