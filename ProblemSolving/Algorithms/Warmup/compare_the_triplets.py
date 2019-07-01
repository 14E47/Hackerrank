A = raw_input().split()
B = raw_input().split()

def comparision(A,B):

    alice = 0
    bob = 0

    for i in range(0,3):

        if int(A[i]) > int(B[i]):
            alice += 1

        elif int(A[i]) < int(B[i]):
            bob += 1

        else:
            alice += 0
            bob += 0

    return alice, bob

result = comparision(A,B)

print(' '.join(str(i) for i in result))