class EquilateralTriangle:

    def __init__(self, side):
        self.side = side

    def __add__(self, other):
        # self.side gets the value from et1 and other.side gets the value from et2
        return self.side * 3 + other.side * 3


et1 = EquilateralTriangle(4)
et2 = EquilateralTriangle(6)

print("Sum of the perimeters of two instances of EquilateralTriangle class:", et1 + et2)
