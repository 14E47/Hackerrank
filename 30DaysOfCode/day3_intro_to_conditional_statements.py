#!/bin/python

import sys


N = int(raw_input().strip())

if N in range(1,100,2):
    print ('Weird')

elif N in range(2,6,2):
    print ('Not Weird')

elif N in range(6,22,2):
    print ('Weird')

elif N in range(20,101,2):
    print ('Not Weird')

