from collections import deque

n,d = map(int,input().split())
elems = list(map(int,input().split()))
z = deque(elems)
for i in range(d):
    z.append(z[0])
    z.popleft()

print(*z)