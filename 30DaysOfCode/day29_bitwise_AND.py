#!/bin/python3

import math
import os
import random
import re
import sys


def max_possible(n,k):
    if k-1|k <= n:
        return k-1
    else:
        return k-2

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(max_possible(n,k))
