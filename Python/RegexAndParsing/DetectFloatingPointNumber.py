import re

def check(N):
    mat = re.match(r'^[-+]?[0-9]*?\.[0-9]+$',N)
    if mat==None:
        return False
    else:
        return True

for i in range(int(input())):
    N = input()
    print(check(N))


