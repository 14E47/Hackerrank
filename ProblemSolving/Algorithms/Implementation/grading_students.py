n = int(raw_input())
grades = []

for _ in xrange(n):
    grades_item = int(raw_input())
    grades.append(grades_item)


for i in range(n):
    if grades[i] < 38:
        print(grades[i])

    else:
        next_multiple = ((grades[i]//5)+1)*5
        diff = next_multiple - grades[i]

        if diff < 3:
            print(next_multiple)


        else:
            print(grades[i])


