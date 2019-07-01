arr = map(int, raw_input().rstrip().split())
arr.sort()


def miniMaxSum(arr):
    max = str(sum(arr[1:]))
    min = str(sum(arr[:4]))

    ans = [min, max]

    result = ' '.join(ans)

    return result


print(miniMaxSum(arr))