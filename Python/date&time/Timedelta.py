import datetime

def time_delta(t1, t2):
    form = "%a %d %b %Y %H:%M:%S %z"
    d1 = datetime.datetime.strptime(t1,form)
    d2 = datetime.datetime.strptime(t2,form)
    diff = int((abs(d1 - d2)).total_seconds())
    print(diff)

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
