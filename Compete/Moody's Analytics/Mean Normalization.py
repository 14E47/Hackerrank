from sys import stdin, stdout

n = int(stdin.readline())

pij = ()
x = []

for a0 in range(n):
    m_i = int(stdin.readline())
    p_i = tuple(map(int, stdin.readline().split()))

    pij += p_i
    x += [sum(p_i) / m_i]

result = 0

for i in x:
    time = 0
    for j in pij:
        time += abs(j-i)

    if result == 0:
        result = time

    elif result > time:
        result = time

stdout.write(str(result)+'\n')
