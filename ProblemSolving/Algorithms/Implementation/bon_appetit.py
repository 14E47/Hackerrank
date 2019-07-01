
def bonAppetit(bill, k, b):
    del bill[k]
    diff = b - sum(bill)//2
    if diff == 0:
        print("Bon Appetit")
    else:
        print(diff)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

