class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    maximumDifference = None

    def compute_difference(self):
        mx = max(self.__elements)
        mn = min(self.__elements)
        self.maximumDifference = mx-mn

