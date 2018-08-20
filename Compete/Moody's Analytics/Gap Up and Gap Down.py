#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(low, high, close):

    gapup = 0
    gapdown = 0

    for i in range(n - 1):
        if low[i + 1] > close[i]:
            gapup += 1
        elif high[i + 1] < close[i]:
            gapdown += 1

    print(gapup, gapdown)

if __name__ == '__main__':
    n = int(input().strip())

    low = list(map(int, input().rstrip().split()))

    high = list(map(int, input().rstrip().split()))

    close = list(map(int, input().rstrip().split()))

    solve(low, high, close)
