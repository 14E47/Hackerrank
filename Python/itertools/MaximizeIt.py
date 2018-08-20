from itertools import product

k,m = map(int,input().split())
li = []
for i in range(k):
    n = list(map(int,input().split()))
    parts = []
    for j in range(1,len(n)):
        x = pow(n[j],2)
        parts.append(x)
    li.append(parts)

z = list(product(*li))

def maximize():
    max_list = []
    for a in z:
        max_list.append(sum(a)%m)
    print(sorted(max_list, reverse=True)[0])

maximize()
