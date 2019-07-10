t = int(input())

for i in range(t):
    s = input()
    n = len(s)

    s1 = ''
    s2 = ''

    for j in range(0,n,2):
        s1 += s[j]

    for k in range(1,n,2):
        s2 += s[k]

    new = [s1,s2]
    res = ' '.join(new)

    print(res)