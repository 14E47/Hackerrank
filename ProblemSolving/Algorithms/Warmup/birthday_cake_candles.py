
n = int(raw_input())
elements = raw_input()
ar = list(map(int, elements.rstrip().split()))

def birthdayCakeCandles(n, ar):
    z = max(ar)
    c = 0
    for i in range(n):
        if z == ar[i]:
            c +=1

    return c

result = birthdayCakeCandles(n, ar)
print(result)