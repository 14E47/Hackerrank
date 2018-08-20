from collections import OrderedDict

n = int(input())
od = OrderedDict()
li = []
for _ in range(n):
    k = input()
    if k not in od.keys():
        od[k] = 1
    else:
        od[k] += 1

print(len(od))
print(*od.values())
