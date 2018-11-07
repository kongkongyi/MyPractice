#!/usr/local/bin/python3
# -*- utf-8 -*- 

if __name__=='__main__':
	unit = ['个','十','百','千','万','十万','百万','千万','亿']
	num = input("Plase input a number:").strip().lstrip('0')
	try:
		if isinstance(int(num), (int)):
			length = len(num) 
			count = [0]*10
			
			print("The length of the number is {}".format(length))

			for j in range(10):
				count[j] = num.count(str(j))

			for x in range(10):
				if int(count[x]) != 0:
					print("digit {} appears {} times".format(x, count[x]))

			for i in range(length):
				print("{}位数值是{}".format(unit[i],num[-1-i]))
		
	except ValueError:
		print("ValueError,retry...") 

