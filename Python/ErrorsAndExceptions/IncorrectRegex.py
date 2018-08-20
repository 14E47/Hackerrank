import re

for i in range(int(input())):
    try:
        z = re.compile(input())
        print(bool(z))
    except re.error:
        print('False')
