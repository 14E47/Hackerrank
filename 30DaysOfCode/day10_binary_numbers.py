# n = 5
#
# print(bin(n).split('b')[1])
#
# x = 101
# print()

#!/bin/python3

import math
import os
import random
import re
import sys

def max_consecutive_ones(n):
    b = bin(n).split('b')[1]
    consecutive_ones = 0
    count = 0
    for i in b:
        if i == '0':
            count = 0
        else:
            count += 1
            consecutive_ones = max(consecutive_ones, count)

    return consecutive_ones

if __name__ == '__main__':
    # n = int(input('Enter n:'))
    n = 5
    n = 13
    n = 7
    n = 8
    n = 15
    print(max_consecutive_ones(n))
