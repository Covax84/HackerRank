class Calculator:

    def power(self, n: int, p: int):
        try:
            if n >= 0 <= p:
                return int(n) ** int(p)
            else:
                raise Exception
        except Exception:
            return 'n and p should be non-negative'


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
