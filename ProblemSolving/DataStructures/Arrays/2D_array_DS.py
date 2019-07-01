#!/bin/python3

import math
import os
import random
import re
import sys


def sub_m(arr, a, b):
    matrix = []
    for i in range(a, a + 3):
        sub = []
        for j in range(b, b + 3):
            sub.append(arr[i][j])
        matrix.append(sub)
    return matrix


# Complete the hourglassSum function below.
def hourglassSum(arr):
    counter = 'wsk'
    for i in range(4):
        for j in range(4):
            hg = sub_m(arr, i, j)
            add = sum(hg[0] + [hg[1][1]] + hg[2])
            if counter == 'wsk':
                counter = add
            else:
                if add > counter:
                    counter = add
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
