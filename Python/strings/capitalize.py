#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    z = s.capitalize()
    new = ''
    c = 0
    for i in z:
        if i==' ':
            new += i
            c = 1
        elif i!=' ' and c==1:
            new += i.upper()
            c = 0
        else:
            new += i

    return new

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')
    #
    # fptr.close()

    print(result)
