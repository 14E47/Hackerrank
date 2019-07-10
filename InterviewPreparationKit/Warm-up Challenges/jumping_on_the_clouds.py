
def jumpingOnClouds(c):
    index = 0
    jumps = 0

    while index!=len(c)-3:
        single = index+1
        double = index+2

        if c[double]!=1:
            jumps += 1
            index += double
        else:
            jumps += 1
            index += single

    print(index,jumps)

    return jumps

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)
