#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    c = 0
    dic = {}
    for i in range(n):
        if ar[i] not in list(dic):
            dic[ar[i]] = 1
        else:
            dic[ar[i]] += 1

    for i in list(dic):
        num = math.floor(dic[i] / 2)
        c += num

    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
