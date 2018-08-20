import re

def fun(s):
    try:
        a = s.index('@')
        b = s.index('.')
        z1 = s[:a]
        z2 = s[a+1:b]
        z3 = s[b+1:]
        match = re.match('^[_a-z0-9-]*@[a-z0-9]*.([a-z]{2,3})$', s)

        if len(z1)!=0 and len(z2)!=0 and len(z3)<=3:
            if match==None:
                return False
            else:
                return True
    except:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)