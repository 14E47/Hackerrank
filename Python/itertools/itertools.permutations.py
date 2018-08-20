from itertools import permutations

r = input().split()
s = sorted(r[0])

k = int(r[1])

li = list(permutations(s,k))

for i in range(len(li)):
    print(*li[i],sep='')
