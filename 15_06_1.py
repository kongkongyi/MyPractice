#!/usr/local/bin/python3
# -*- coding:utf-8 -*-


def dictflat(src, dst, nkey = []):
    src_len = len(src)
    i = 0

    for k, v in src.items():
        nkey.append(k)

        if isinstance(v, (dict,)):
            nkey.append('.')
            print('_nkey:{}, _dst:{}'.format(nkey, dst))
            dictflat(v, dst, nkey)
        else:
            print('_nkey:{}, _dst:{}'.format(nkey, dst))

            dst[''.join(nkey)] = v

            #print('_nkey:{}, _dst:{}'.format(nkey, dst))

            nkey.pop() 
            i += 1

            print('src_len:{}, num_i:{},  _nkey:{}, _dst:{}'.format(src_len, i, nkey, dst))

            if src_len == i:
                nkey.clear() 
                print('src_len:{}, num_i:{},  _nkey:{}, _dst:{}'.format(src_len, i, nkey, dst))


    #print(dst)
        


if __name__=='__main__':
    #src = {'a':{'t':10,'b':{'c':{'h':{'m':3}}}}, 'd':{'e':3, 'f':{'g':{'k':{'w':4}}}}}
    src = {'a':{'b':1, 'c':2}, 'd':{'f':{'g':{'a':4, 'b': 5}}, 'm':7}} 
    dst = {}
    dictflat(src, dst)
    print(dst)
