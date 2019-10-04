#!/bin/python3

import math
import os
import random
import re
import sys


def regex(emailId):
    p = '@gmail.com'
    match = re.search(p, emailId)
    return match


if __name__ == '__main__':
    N = int(input())

    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if regex(emailID) is not None:
            names.append(firstName)

    names.sort()
    for i in names:
        print(i)
