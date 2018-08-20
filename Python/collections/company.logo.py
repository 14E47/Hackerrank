from collections import Counter

def choose(elem):
    return elem[1]

def logo():
    se = Counter(s)
    z = se.most_common()
    print(z)
    print(max(z))
    for i in range(3):
        if z[0][1] == z[1][1]:
            x = sorted(z)
            for j in range(len(x)):
                if x[j][1] == z[0][1]:
                    print(x[j][0],x[j][1])
                    indi = z.index(x[j])
                    z.pop(indi)
                    break
        else:
            print(z[0][0],z[0][1])
            z.pop(0)

if __name__ == '__main__':
    s = input()
    logo()

