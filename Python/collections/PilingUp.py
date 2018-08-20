from collections import deque

def pile():
    check = 0
    while len(d) > 1:
        l = d[0]
        r = d[-1]
        if l > r and check == 0:
            check = l
            d.popleft()
        elif r > l and check == 0:
            check = r
            d.pop()
        elif r == l and check == 0:
            check = r
            d.pop()
        else:
            if l > r:
                if l > check:
                    return 'No'
                else:
                    check = l
                    d.popleft()
            elif r > l:
                if r > check:
                    return 'No'
                else:
                    check = r
                    d.pop()
            else:
                if r > check:
                    return 'No'
                else:
                    check = r
                    d.pop()

    return 'Yes'

for i in range(int(input())):
    n = int(input())
    d = deque(map(int,input().split()))
    print(pile())
