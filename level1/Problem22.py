# -*- coding:utf-8 -*-

'''
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

fileHandle = open ( '../files/p022_names.txt') 
nameLine = fileHandle.readline()

names = sorted(nameLine.split(","))

def get_alpha_order(c):
	order_val = ord(c)
	if order_val >= 96:
		return order_val - 96
	else:
		return order_val - 64


def get_name_sum(name):
	name = name.replace('\"', "").replace("\s+", "")
	return sum([get_alpha_order(c) for c in name])


result = 0
for i in range(len(names)):
	score = (i+1) * get_name_sum(names[i])
	#print i+1, names[i], get_name_sum(names[i]), score
	result += score

print result

#print get_name_sum('"MARY"'), map(get_alpha_order, '"MARY"')