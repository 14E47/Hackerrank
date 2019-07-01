
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    res = [0,0,0,0,0]

    for i in arr:
        res[i-1] += 1

    return res.index(max(res))+1

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

