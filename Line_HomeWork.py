class Line():

    def __init__(self, coordinate_1, coordinate_2):
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2

    def distance(self):

        x1,y1 = self.coordinate_1
        x2,y2 = self.coordinate_2

        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):

        x1,y1 = self.coordinate_1
        x2,y2 = self.coordinate_2

        return (y2-y1) / (x2-x1)

c1 = (3,2)
c2 = (8,10)

my_line = Line(c1,c2)

print(my_line.distance())
print(my_line.slope())
        