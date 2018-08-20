s = input()
x = sorted(s)
s1 = ''
s2 = ''
s3 = ''
s4 = ''

for i in x:
    if i.islower():
        s1 += i
    elif i.isupper():
        s2 += i
    elif i.isnumeric() and int(i) in range(1,10,2):
        s3 += i
    elif i.isnumeric() and int(i) in range(0,10,2):
        s4 += i

print(s1+s2+s3+s4)