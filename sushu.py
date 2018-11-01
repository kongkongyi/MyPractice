#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import math
reslt = []
for n in range(2,100):
	for j in reslt:
		if n % j == 0:
			break
	else:
	#	print (n)
		reslt.append(n)
print (reslt)
