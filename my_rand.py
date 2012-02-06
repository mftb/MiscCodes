#!/usr/bin/env python
# -*- coding: latin1 -*-

def my_rand():
#    k = 31247513
    k = 56789012386421
    q = 103511
    a = k % q
    while True:
        yield a
        a, k = (a + k) % q, a

r = my_rand()
for i in range(0,101):
#while True:
    print (r.next()/103511.0)
