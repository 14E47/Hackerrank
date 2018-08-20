s = 'BANANA'

def minion_game(s):
    vowels = 'AEIOU'
    c1 = 0
    c2 = 0
    t = len(s)
    for i in range(t):
        if s[i] not in vowels:
            c1 += t - i
        else:
            c2 += t - i


    if c1 > c2:
        print('Stuart %s' %c1)
    elif c2 > c1:
        print('Kevin %s' %c2)
    else:
        print('Draw')

minion_game(s)