
def count(n):
    c = 0
    while n != 0:
        c += 1
        n //= 10

    return c

n = int(input())
print(count(n))


