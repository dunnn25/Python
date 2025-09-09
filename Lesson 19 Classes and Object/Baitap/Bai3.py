###Bài 3: Kế thừa và đa hình - Hệ Thống Hình Học
import  math

class Shape:
    def __init__(self):
        pass
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__()
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius

Rectangle1 = Rectangle(5,5)
Circle1 = Circle(3)
var = [Rectangle1,Circle1]
for i in var:
    if isinstance(i, Rectangle):
        print("Diện tích Rectangle: ",i.area())
    elif isinstance(i, Circle):
        print("Diện tích Circle: ",i.area())

