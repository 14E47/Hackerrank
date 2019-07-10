#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):

    if n<=1:
        return 1
    else:
        fac = n*factorial(n-1)
        return fac

n = int(input("Enter factorial no. :"))
result = factorial(n)
print(result)

