n = int(raw_input())
arr = map(int, raw_input().rstrip().split())

pos = float(0)
neg = float(0)
zero = float(0)

for i in range(n):

    if arr[i] > 0:
        pos +=1

    elif arr[i] < 0:
        neg += 1

    else:
        zero += 1

a1 = round((pos/n),n)
a2 = round((neg/n),n)
a3 = round((zero/n),n)

print(a1)
print(a2)
print(a3)

