n,x = map(int,input().split())

li = []
for i in range(x):
    li.append(list(map(float,input().split())))

zipped = list(zip(*li))

for j in range(n):
    print(sum(zipped[j])/x)
