class AdvancedArithmetic(object):
    def divisor_sum(self, n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisor_sum(self, n):
        divisors = []
        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisor_sum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
