def fine(actual, expected):
    d1, m1, y1 = actual[0], actual[1], actual[2]
    d2, m2, y2 = expected[0], expected[1], expected[2]

    if y1 < y2:
        return 0
    elif y1 > y2:
        return 10000
    elif y1 == y2:
        if m1 <= m2:
            if d1 > d2:
                return 15*(d1-d2)
            else:
                return 0
        else:
            return 500*(m1-m2)


date1 = list(map(int, input().split()))
date2 = list(map(int, input().split()))
print(fine(date1, date2))


# 10 10 2019
# 10 12 2019