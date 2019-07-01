n = int(raw_input())

a = []

for _ in xrange(n):
    a.append(map(int, raw_input().rstrip().split()))

def diagonalDifference(a):

    d1 = sum(a[i][i] for i in range(n))
    d2 = sum(a[i][n-i-1] for i in range(n))

    return abs(d1-d2)

result = diagonalDifference(a)
print(result)
