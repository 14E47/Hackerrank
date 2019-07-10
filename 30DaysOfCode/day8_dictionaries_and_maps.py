
phonebook = {}

n = int(input())
for i in range(n):
    name_phone = input().split()
    phonebook[name_phone[0]] = name_phone[1]

while True:
    try:
        query = input()
        try:
            print(f'{query}={phonebook[query]}')
        except:
            print('Not found')
    except:
        break

# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry