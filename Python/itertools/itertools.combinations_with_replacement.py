from itertools import combinations_with_replacement

r = input().split()
s = sorted(r[0])

k = int(r[1])

li = list(combinations_with_replacement(s,k))

for i in range(len(li)):
    print(*li[i],sep='')
