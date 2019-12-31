class Difference:
    def __init__(self, a: list):
        self.__elements = a
        self.maximumDifference = self.compute_difference()

    def compute_difference(self) -> int or float:
        return max(self.__elements) - min(self.__elements)


# End of Difference class

# _ = input()
# a = [int(e) for e in input().split(' ')]
a = [1, 2, 3, 4, 5]

d = Difference(a)
d.compute_difference()

print(d.maximumDifference)
