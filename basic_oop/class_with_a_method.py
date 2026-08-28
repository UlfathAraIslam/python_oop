class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def get_area(self):
        print(self.width * self.height)
rectangle1 = Rectangle(10,5)
rectangle2 = Rectangle(8,4)
rectangle1.get_area()
rectangle2.get_area()