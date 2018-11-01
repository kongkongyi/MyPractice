#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import random

def BubbleSort(num):
	tmp=0
	swap_count=0
	count=0
	loop=len(num)-1
	flag=False
	while loop>0:
		flag=False
		#print(loop)
		for j in range(loop):
			count += 1
			if num[-1-j] < num[-1-j-1]:
				swap_count += 1
				tmp = num[-1-j]
				num[-1-j] = num[-1-j-1]
				num[-1-j-1] = tmp
				flag=True
			#print (j,num[-1-j], num[-1-j-1], num)
		if not flag:
			break
		loop -= 1

	print(count, swap_count, num)
			

if __name__=='__main__':
	num=[1,2,3,4,5,6,7,8,9,0,10,11,12,13,14]
	#num=[1,2,3,4,5]
	random.shuffle(num)
	print(num)
	BubbleSort(num)
