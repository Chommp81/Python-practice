def draw_board():
	#Take user input and check for integer
	while True:
		try: 
			c = input("How many columns across? ")
			r = input("How many rows down? ")
			break
		except NameError:
			print "Sorry, you didn't enter an integer"
			pass

	for i in range(r):
		print " ---"*c
		print "|   "*c + "|"
	print " ---"*c

draw_board()

