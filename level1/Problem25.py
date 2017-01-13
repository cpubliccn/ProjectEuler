# -*- coding:utf-8 -*-

'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
import time

def fab(max): 
   n, a, b = 0, 0, 1 
   while n < max: 
       yield b 
       # print b 
       a, b = b, a + b 
       n = n + 1 

start = time.time()
my_f = fab(100000)

n = 0
while True:
	n += 1
	num = my_f.next()
	if len(str(num)) >= 1000:
		break

end = time.time()
print end - start, n
