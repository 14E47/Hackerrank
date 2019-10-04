 #Write your code here
class Calculator:

    def power(self, x, y):
        if x < 0 or y < 0:
            raise ValueError('n and p should be non-negative')
        return pow(x,y)

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)

