
def countingValleys(n, s):
    sigma = 0
    valleys = 0
    for i in s:
        if i == 'U':
            previous = sigma
            sigma += 1
            if previous < 0 and sigma == 0:
                valleys += 1

        if i == 'D':
            previous = sigma
            sigma += -1
            if previous < 0 and sigma == 0:
                valleys += 1

    return valleys

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)
