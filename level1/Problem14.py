# -*- coding:utf-8 -*-

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import time

start = time.time()
data = {}


def get_chain_length(n, a):
    if data.has_key(n):
        return len(a) + data.get(n)
    if n == 1:
        return len(a)
    if n % 2 == 0:
        n /= 2
    else:
        n = 3*n + 1
    a.append(n)
    return get_chain_length(n, a)


for i in range (13, 1000000, 2):
    l = get_chain_length(i ,[])
    data[i] = l

data = sorted(data.iteritems(), key=lambda d:d[1], reverse = True)

end = time.time()

print end - start, data[0], data[1]