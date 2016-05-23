"""
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!
"""

def maxofthree ():
	#check that inputs are integers
	while True:
		try:
			a = input("First number please:")
			b = input("Second number:")
			c = input("Third number:")
			break
		except NameError:
			return "Oops! Not a valid number"	

	#check which number is largest
	if a > b and a > c:
		return a
	elif b > a and b > c:
		return b
	elif c > a and c > b:
		return c
	else:
		return "There is no single largest number. Two or more numbers are equally largest"

print maxofthree()