
t = raw_input()

def TimeConversion(t):
    deciding_f = t[8:]
    if deciding_f == 'AM':
        if int(t[:2]) == 12:
            return ("00"+ t[2:8])

        else:
            return t[:8]

    else:
        if int(t[:2]) != 12 :
            hour = int(t[:2]) + 12
            return (str(hour)+ t[2:8])

        else:
            return (t[:8])

result = TimeConversion(t)
print(result)