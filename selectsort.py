#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

def SelectSort(num):
    print(num)
    pos = 0
    for i in range(len(num)):
        min = num[i]
        for j in range(i+1, len(num)):
            if num[j] < min: 
                print("Min.{}, Pos.{}".format(min, pos))
                min = num[j]
                pos = j
                
        num[pos] = num[i]
        num[i] = min
        print(num)

if __name__=='__main__':
    lists = [[1,2,3,4,5,6,7,8,9],
             [9,8,7,6,5,4,3,2,1],
             [7,5,4,3,8,1,2,6,9]]
    SelectSort(lists[0])
    
            
