import re

S = input()
k = input()


for i in range(len(S)):
    m = re.search(k,S)
    print(m.start())

# print(m.start(1))
# print(m.end())