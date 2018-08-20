from itertools import groupby

r = input()

li = ()

for i,k in groupby(r):
    print((len(list(k)),int(i)), end=' ')

