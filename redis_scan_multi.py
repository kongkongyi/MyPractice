#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import redis
import subprocess
import time
import threading


def ConnectRedis(ip, port, auth):
    r = redis.StrictRedis(ip, port, password=auth)
    i = 0

    for key in r.scan_iter(match='prefix_share_p:*'):
        if i>1000:
            i=0
            time.sleep(0.5)

        with open('/home/dump/{}_{}'.format(ip, port), 'a') as f:
            f.write("{}{}".format(key, '\n'))

        r.delete(key)

        #print("KEY:{}".format(key))

        i += 1

if __name__=='__main__':
    host_prefix = 'lottery-abc-'
    
    for x in range(1,41,5):
        thrs = [threading.Thread(target=ConnectRedis, args=['{}{}'.format(host_prefix, i), '3000{}'.format(j), 'pwd']) for i in range(x, x+5) for j in range(1,3)]
        [thr.start() for thr in thrs]
        [thr.join() for thr in thrs]
