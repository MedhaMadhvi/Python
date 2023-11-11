# Write a Python program to create a class named Rectangle with attributes length and width. Implement methods to calculate the area and perimeter of the rectangle. Also, implement a method to compare two rectangles based on their area.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def compare_area(self, other):
        area1 = self.calculate_area()
        area2 = other.calculate_area()
        if area1 > area2:
            return "The first rectangle is larger."
        elif area1 < area2:
            return "The second rectangle is larger."
        else:
            return "Both rectangles have the same area."

length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))
rectangle1 = Rectangle(length1, width1)

length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))
rectangle2 = Rectangle(length2, width2)


area1 = rectangle1.calculate_area()
perimeter1 = rectangle1.calculate_perimeter()
print(f"Rectangle 1: Area = {area1}, Perimeter = {perimeter1}")

area2 = rectangle2.calculate_area()
perimeter2 = rectangle2.calculate_perimeter()
print(f"Rectangle 2: Area = {area2}, Perimeter = {perimeter2}")


comparison_result = rectangle1.compare_area(rectangle2)
print(comparison_result)