from operator import itemgetter

n,m = map(int,input().split())
li = []
for i in range(n):
    mi = list(map(int,input().split()))
    li.append(mi)

k = int(input())
result = sorted(li,key=itemgetter(k))

for i in range(n):
    print(*result[i])