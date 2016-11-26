# -*- coding:utf-8 -*-

'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''

limit = 4000000
a = [1,2]
x = a[-1] + a[-2]
while x <= limit:
    a.append(x)
    x = a[-1] + a[-2]

print(sum([y for y in a if y % 2 == 0]))