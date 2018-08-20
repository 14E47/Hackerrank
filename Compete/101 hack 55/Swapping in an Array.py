
def swapToSort(a):
    print(sorted(a))

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = swapToSort(a)

