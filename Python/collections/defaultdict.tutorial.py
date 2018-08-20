from collections import defaultdict
d = defaultdict(list)

n,m = map(int,input().split())
for _ in range(n):
    d['A'].append(input())
for _ in range(m):
    d['B'].append(input())

for i in range(m):
    answer = []
    neg_answer = []
    for j in range(n):
        if d['B'][i] == d['A'][j]:
            answer.append(j+1)
        elif d['B'][i] not in d['A']:
            neg_answer.append(-1)
            break
    if len(answer)==0:
        print(*neg_answer)
    else:
        print(*answer)
