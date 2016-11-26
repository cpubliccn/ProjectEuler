# -*- coding:utf-8 -*-

'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def isPalindromic(n):
    s = str(n)
    l = len(s)
    if l % 2 != 0:
        return False
    for i in range(l/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

a = []

for x in range(999, 100, -1):
    for y in range(x, 100, -1):
        if isPalindromic(x*y):
            a.append(x * y)
            break

print(max(a))
