from collections import namedtuple

N = int(input())
Students = namedtuple('Students',input())
s = 0
for _ in range(N):
    s += int(Students(*(input().split())).MARKS)

print(round(s/N,2))