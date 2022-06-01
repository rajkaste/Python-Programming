class Polygon:
    sides_len = []

    def __init__(self, no_of_sides):
        self.no_of_sides = no_of_sides
        print("Polygon of {} sides".format(self.no_of_sides))

    def inputSides(self):
        while True:
            length = float(input("Enter length:"))
            self.sides_len.append(length)
            self.no_of_sides -= 1
            if self.no_of_sides == 0:
                break
        return self.sides_len

    def dispSides(self):
        for index, length in enumerate(self.sides_len):
            print(index+1, "->", length)


hexagon = Polygon(6)

hexagon.inputSides()
print("Polygon side with its length respectively:")
hexagon.dispSides()
