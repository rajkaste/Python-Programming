class Polygon:
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3


class Triangle(Polygon):
    def findPerimeter(self):
        sum_of_sides = self.l1 + self.l2 + self.l3
        return sum_of_sides

    def findArea(self):
        # s = semi-perimeter
        s = self.findPerimeter() / 2
        area = (s * (s - self.l1) * (s - self.l2) * (s - self.l3)) ** 0.5
        return area


class EquilateralTriangle(Triangle):

    def __init__(self, side):
        self.side = side

    def findPerimeter(self):
        return self.side * 3


t = Triangle(8, 4, 6)
print("Perimeter of Triangle: ", t.findPerimeter())
et = EquilateralTriangle(5)
print("Perimeter of Equilateral Triangle: ", et.findPerimeter())
