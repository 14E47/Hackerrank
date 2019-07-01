
def breakingRecords(scores):

    high = scores[0]
    low = scores[0]

    c1 = 0
    c2 = 0

    for i in scores:
        if i > high:
            c1 += 1
            high = i
        elif i < low:
            c2 += 1
            low = i

    return c1,c2

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
