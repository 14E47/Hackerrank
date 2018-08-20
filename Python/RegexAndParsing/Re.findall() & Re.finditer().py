import re

s = input()
m = re.findall(r'(([aeiouAEIOU]){2,})', s)
print(m)

# z = list(map(lambda x: x.group(),m))
# print(z)
if len(m)==0:
   print(-1)
else:
    for i in m:
        print(i[0])
