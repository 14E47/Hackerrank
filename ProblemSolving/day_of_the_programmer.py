
def dayOfProgrammer(year):
    if year == 1918:
        return f"26.09.{year}"
    elif year > 1918:
        if year % 400 == 0:
            return f"12.09.{year}"
        elif year % 4 == 0 and year % 100 != 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    else:
        if year % 4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)