#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    c = 0

    while True:
        swapped = False
        for i in range(len(q)-1):
            if q[i]>q[i+1]:
                q[i],q[i+1] = q[i+1], q[i]
                swapped = True
                c += 1

        if not swapped:
            break

    return c

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
