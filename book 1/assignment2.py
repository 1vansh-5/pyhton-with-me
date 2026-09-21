# Question - take diameter as a input and  find the area of the circle\
diameter = int(input("Enter the diameter of the circle :"))

radius = diameter/2

area = 3.14 * (radius ** 2)
print("Radius of the circle is", radius)
print("The area of the circle is :", area)
