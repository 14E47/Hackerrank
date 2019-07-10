
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

new = []

for i in range(1,n+1):
    new.append(str(arr[-i]))

res = ' '.join(new)
print(res)
