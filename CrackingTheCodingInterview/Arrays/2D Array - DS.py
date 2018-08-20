arr = []

for i in range(6):
    arr += [list(map(int,input().split()))]

print(arr)

sub = 0
x, y = 0, 0
for j in arr:
    c1 = 0
    for k in j:
        while c1 in range(0,3,2):

