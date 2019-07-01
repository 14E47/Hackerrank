#!/bin/python3

import math
import os
import random
import re
import sys

def rotation(d,a):
    for i in range(d):
        ini = a.pop(0)
        a.append(ini)
    return a

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = input().rstrip().split()

    print(' '.join(rotation(d,a)))
