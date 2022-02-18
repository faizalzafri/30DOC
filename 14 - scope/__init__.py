class Difference:
    def __init__(self, a):
        self.maximumDifference = -63
        self.__elements = a

    # Add your code here
    def computeDifference2(self):
        for i in range(0, len(self.__elements)):
            for j in range(i + 1, len(self.__elements)):
                current_diff = abs(self.__elements[i] - self.__elements[j])
                if current_diff > self.maximumDifference:
                    self.maximumDifference = current_diff

    def computeDifference(self):
        min_num = 101
        max_num = 0
        for number in self.__elements:
            if number < min_num:
                min_num = number
            if number > max_num:
                max_num = number

        self.maximumDifference = max_num - min_num


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
