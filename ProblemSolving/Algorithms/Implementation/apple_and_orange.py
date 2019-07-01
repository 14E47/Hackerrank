
import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    c1 = 0
    c2 = 0
    frange = range(s,t+1)

    for x in range(m):
        if a+apples[x] in frange:
            c1 += 1

    for x in range(n):
        if b+oranges[x] in frange:
            c2 += 1

    stat1 = print(c1)
    stat2 = print(c2)

    return stat1,stat2

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
