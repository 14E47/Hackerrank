N, n = int(input()), list(map(int, input().rstrip().split()))
print(all([i>0 for i in n]) and any([str(i)==str(i)[::-1] for i in n]))

