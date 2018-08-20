from itertools import combinations

r = input().split()
s = sorted(r[0])

k = int(r[1])


for i in range(k):
    li = list(combinations(s,i+1))
    for j in range(len(li)):
        print(*li[j],sep='')
