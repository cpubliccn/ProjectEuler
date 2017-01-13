# -*- coding:utf-8 -*-

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

import time

start_time = time.time()

d = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", \
	"8":"eight", "9":"nine", "10":"ten", "11":"eleven", "12":"twelve", "13":"thirteen", "14":"fourteen", \
	"15":"fifteen", "16":"sixteen", "17":"seventeen", "18":"eighteen", "19":"nineteen", "20":"twenty", \
	"30":"thirty", "40":"forty", "50":"fifty", "60":"sixty", "70":"seventy", "80":"eighty", "90":"ninety"}

def get_thousands_words(n):
	n_thousands = n / 1000
	words = ""
	if n_thousands > 0:
		words = d[str(n_thousands)] + " thousand "
		if n % 1000 > 0:
			words += "and " + get_hundreds_words(n - n_thousands * 1000)
	return words


def get_hundreds_words(n):
	n_hundreds = n / 100	
	words = ""
	if n_hundreds > 0:
		words = d[str(n_hundreds)] + " hundred "
		if n % 100 > 0:
			words += "and " + get_tens_words(n - n_hundreds * 100)
	return words

def get_tens_words(n):
	if d.has_key(str(n)):
		return d[str(n)]
	else:
		n_tens = (n / 10) * 10
		words = d[str(n_tens)]
		if n % 10 > 0:
			words += "-" + d[str(n%10)]
		return words


def get_words(n):
	if n < 100:
		return get_tens_words(n)
	elif n < 1000 and n >= 100:
		return get_hundreds_words(n)
	else:
		return get_thousands_words(n)


a = [get_words(n) for n in range(1, 1001)]

len_a = [len(x.strip().replace(" ", "").replace("-", "")) for x in a]

print sum(len_a)
end_time = time.time()
print end_time - start_time
