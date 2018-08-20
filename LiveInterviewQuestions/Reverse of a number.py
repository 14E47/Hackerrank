number = int(input())

rev = 0

while number>0:
    rem = number%10
    rev = rev*10 + rem
    number//= 10

print(rev)