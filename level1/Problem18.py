# -*- coding:utf-8 -*-

'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)
'''

text_array = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''.strip().split("\n")

a = [[int(x) for x in line.strip().split(" ")] for line in text_array]
l = len(a)

def process():
	for row in range(l-1, 1, -1):
		row_length = len(a[row])
		for col in range(0, row_length):
			#print row,col,a[row][col]
			if col == 0 and a[row][col] < a[row][col+1]:
				a[row][col] = 0
			elif col == row_length - 1 and a[row][col] < a[row][col - 1]:
				a[row][col] = 0
			else:
				if col > 1 and col < row_length -1:
					if row == 14 and col == 13:
						print a[row][col], a[row][col-1], a[row][col+1]
					if a[row][col] < a[row][col-1] and a[row][col] < a[row][col+1]:
						a[row][col] = 0


def print_array(a):
	for row in a:
		print row

def pre_process():
	for row in range(l-1, 0, -1):
		row_length = len(a[row])
		for col in range(0, row_length-1):
			a[row-1][col] += (a[row][col] > a[row][col+1] and a[row][col] or a[row][col+1])
		#print_array(a)

pre_process()
print a[0][0]