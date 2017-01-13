# -*- coding:utf-8 -*-

'''
You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

years = range(1901, 2001)
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
	if year % 100 == 0:
		return year % 400 == 0
	else:
		return year % 4 == 0


def days_of_year(year):
	if is_leap_year(year):
		return 366
	else:
		return 365


cnt = 0
start = days_of_year(1900) + 1
for year in range(1901, 2001):
	for month in range(0,12):
		if start % 7 == 0:
			cnt += 1
		days = days_of_month[month]
		if is_leap_year(year) and month == 1:
			days += 1
		start += days;


print cnt