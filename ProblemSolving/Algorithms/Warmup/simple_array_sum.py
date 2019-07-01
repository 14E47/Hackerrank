ar_count = int(raw_input())
ar = map(int, raw_input().rstrip().split())

def simpleArraySum(ar):

    return sum(ar,0)


result = simpleArraySum(ar)

print(result)
