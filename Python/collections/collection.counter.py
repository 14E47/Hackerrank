from collections import Counter

money = []
def total_amount(req_size,price):
    if group[req_size] != 0 :
        group[req_size] -= 1
        money.append(price)

x = int(input())
sizes = map(int,input().split())
group = Counter(sizes)
n = int(input())
for _ in range(n):
    req_size, price = map(int,input().split())
    total_amount(req_size,price)
print(sum(money))