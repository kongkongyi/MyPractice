#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

nums = []
while len(nums) < 5:
    num = input("Please input a numer:").strip().lstrip('0')
    if not num.isdigit():
        continue
    print("The length of {} is {}".format(num, len(num)))
    nums.append(int(num))

print(nums)        	
