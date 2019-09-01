#!/bin/python3

import math
import os
import random
import re
import sys

def max_hourglass_sum(a):

    maxx = None
    for r in range(4):
        for c in range(4):
            sub = []
            sub.append(a[r][c:c+3])
            sub.append(a[r+1][c:c+3])
            sub.append(a[r+2][c:c+3])

            sigma = sum(sub[0])+ sub[1][1] + sum(sub[2])
            if maxx is None:
                maxx = sigma
            else:
                if sigma > maxx:
                    maxx = sigma
    return maxx







if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(max_hourglass_sum(arr))
