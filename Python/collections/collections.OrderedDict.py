from collections import OrderedDict

N = int(input())
OD = OrderedDict()
for _ in range(N):
    rinp = input().rpartition(' ')
    item_name = rinp[0]
    net_price = int(rinp[2])
    if item_name not in OD.keys():
        OD[item_name] = net_price
    else:
        OD[item_name] += net_price

for _ in OD:
    print(_, OD[_])
