n = int(raw_input())

d = '#'
for i in range(1,n+1):
    width = n
    print((d*i).rjust(width, ' '))

