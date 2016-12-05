# -*- coding:utf-8 -*-

import time

l = 20
a =  [[0 for col in range(l+1)] for row in range(l+1)]

def get_path_cnt((start_x, start_y), (end_x, end_y)):
    cnt = 0
    if start_x == end_x or start_y == end_y:
        cnt = 1
    else:
    	if a[start_x][start_y] != 0:
    		cnt = a[start_x][start_y]
    	else:
        	cnt = get_path_cnt((start_x+1, start_y), (end_x, end_y)) + get_path_cnt((start_x, start_y+1), (end_x, end_y))
    a[start_x][start_y] = cnt
    return cnt


start_time = time.time()
patch_cnt = get_path_cnt((0,0), (l, l))
end_time = time.time()
print "path_count:", patch_cnt, "time:", end_time - start_time