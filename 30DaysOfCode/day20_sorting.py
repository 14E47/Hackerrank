#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

total_swaps = 0
for i in range(n):
    swaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swaps += 1

    total_swaps += swaps
    if swaps == 0:
        break

print(f'Array is sorted in {total_swaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')


