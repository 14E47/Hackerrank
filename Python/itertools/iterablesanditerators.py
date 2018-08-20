from itertools import combinations

n = int(input())
li_n = input().split()
k = int(input())

indices = []
li = []
c = 0
for i in range(n):
    li.append(i+1)
    if li_n[i] == 'a':
        indices.append(i+1)

combs = list(combinations(li,k))
for j in range(len(combs)):
    for k in range(len(indices)):
        if indices[k] in combs[j]:
            c += 1
            break
frac = c/len(combs)
print(round(frac,3))
# print(combs)
# print(c)
# print(len(combs))

# li = [(1, 2, 3, 4), (7, 2, 4, 5), (7, 2, 3, 6), (7, 2, 4, 7), (1, 2, 3, 8), (1, 2, 3, 9), (1, 2, 4, 5)]
# ind = [1,4]
# c = 0
#
# k = len(li)
# l = len(ind)
# for i in range(k):
#     for j in range(l):
#         if ind[j] in li[i]:
#             c += 1
#             break
# print(c)