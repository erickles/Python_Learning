class Circle():

    # Class object attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Method
    def get_circunference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)

print(my_circle.get_circunference())
print(my_circle.area)