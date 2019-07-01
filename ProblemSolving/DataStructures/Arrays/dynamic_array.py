#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    for i in queries:

        q, x, y = i[0], i[1], i[2]
        ind = (x ^ lastAnswer) % n
        if q == 1:
            s = seqList[ind]
            s.append(y)
        elif q == 2:
            s = seqList[ind]
            lastAnswer = s[y % len(s)]
            yield lastAnswer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
