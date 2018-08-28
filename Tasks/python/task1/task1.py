x = int(input("enter a number from 0 to 100"))
if x >= 100 or x < 0:
	print("Error:Input is not a two-digit number.")
elif x == 0:
	print("The tens digit is 0, and the ones digit is 0")
elif x > 0 and x < 10:
	print("The tens digit is 0, and the ones digit is ",x)
elif x > 10:
	y = str(x)
	print("The tens digit is " , y[0] , " , and the ones digit is " , y[1])
