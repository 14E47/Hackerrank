from sys import stdin, stdout
t = int(stdin.readline())

for t_itr in range(t):

    n = int(stdin.readline())

    carry = 0
    for z in range(n):
        profits = [int(x) for x in stdin.readline().split()]
        baaki = (carry + profits[1]) - profits[0]
        carry = max(baaki,0)

    if carry > 0:
        stdout.write(str(1) +'\n')
    else:
        stdout.write(str(0) +'\n')
