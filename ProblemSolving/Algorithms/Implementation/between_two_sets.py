import os
import sys
import math

def getTotalX(a, b):
    g = math.gcd(a[0],a[1])
    lcm = (a[0]*a[1])/g

    print(g)
    print(lcm)

    return lcm

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

