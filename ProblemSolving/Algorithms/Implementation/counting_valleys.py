#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sigma = 0
    valleys = 0
    for i in s:
        if i == 'U':
            previous = sigma
            sigma += 1
            if previous < 0 and sigma == 0:
                valleys += 1

        if i == 'D':
            previous = sigma
            sigma += -1
            if previous < 0 and sigma == 0:
                valleys += 1

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
