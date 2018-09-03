import math
class shape:
	def __init__(self,x):
		self.x = x
	def area (x):
		return x
	def perimeter(x):
		return x
class circle(shape):
	def area (self):
		return (math.pi)*x*x
	def perimeter(self):
		return (math.pi)*2*x
class square(shape):
	def area (self):
		return x*x
	def perimeter (self):
		return 4*x 
x = input("enter which shape you want to calculate it's area and perimeter ")
if x == "circle":
	y = float(input("enter it's raduis "))
	circle1 = circle(y)
	print("your circle's area is ",circle1.area())
	print("your circle's perimeter is ",circle1.perimeter())
if x == "square":
	y = float(input("enter it's length"))
	square1 = square(y)
	print("your square's area is ",square1.area())
	print("your square's perimeter is ",square1.perimeter())

