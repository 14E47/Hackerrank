
def divisibleSumPairs(n, k, ar):

    c = 0
    while len(ar)!=1:
        i = ar.pop(0)
        for j in ar:
            if (i+j)%k == 0:
                c += 1
    return c

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)