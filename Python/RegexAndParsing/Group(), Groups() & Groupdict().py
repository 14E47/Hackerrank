import re

s = input()

m= re.findall(r'(([0-9a-zA-Z])\2)', s)

if len(m)==0:
   print(-1)
else:
    print(m[0][1])
