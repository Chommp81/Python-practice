#http://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
def createboard():
	#when called, creates the board for the game
	global board
	board = []
	for x in range(3):
		board.append(["-","-","-"])
	return board

def print_board():
	#prints the board in an easy to read format
	print board[0]
	print board[1] 
	print board[2]
	

def count_remaining():
	#Keeps track of the number of free spaces left on the board
	count = 0
	for i in range (3):
		count += board[i].count("-")
	return count

def tttdraw():
	#first, create blank board
	import time
	board = createboard()
	
	#initialize the counters
	count = count_remaining() #this counts remaining free spaces
	turn = 0 #this tracks the turn number to figure out whose turn it is

	#This is the loop for each round
	while count > 0:

		#Figure out whose turn it is and set their marker
		if turn % 2 == 0:
			print "PLAYER 1:"
			marker = "X"
		else: 
			print "PLAYER 2:"
			marker = "O"
		
		#keep looping until players guess is valid
		valid_move = False
		while not valid_move:
			#Get players desired coordinates
			row = input("Please input a row between 1 and 3: ") - 1
			col = input("Please input a col between 1 and 3: ") - 1

			#Check coords are empty, and if so add the right marker to the right spot
			if board[row][col] == "-":
				board[row][col] = marker
				print_board()
				valid_move = True
			else: #then coordinates must already have a marker in there
				print "Sorry, that cell is taken. Have another go."

		#Check to see if there was an early winner
		if checkwin(board) != 0 and checkwin(board) != 2:
			print "%s is the winner!" % (checkwin(board))
			count = 0
			return True

		count = count_remaining()
		turn += 1
	
	print "GAME OVER"
	if checkwin(board) == 0:
		print "Nobody won. :("
		
	


def checkwin(array):
	#check that the array is 3 x 3
	if len(array) > 3:
		return "Sorry, the array isn't the right size for Tic Tac Toe"

	#split array into more manageable rows
	toprow = array[0]
	middlerow = array[1]
	bottomrow = array[2]

	#create empty winner list
	winner = []

	#check horizontals
	for i in array:
		if i[0] == i[1] == i[2] and i[0] != "-":
			winner.append(i[0])
			method = "horizontal"

	#check verticals
	for i in range(0,3):
		if array[0][i] == array[1][i] == array[2][i] and array[0][i] != "-":
			winner.append(array[0][i])
			method = "vertical"
	
	#check diagonal top left to bottom right
	if array[0][0] == array[1][1] == array[2][2] and array[0][0] != "-":
		winner.append(array[0][0])
		method = "diagonal"

	#check diagonal bottom left to top right
	if array[0][2] == array[1][1] == array[2][0] and array[0][2] != "-":
		winner.append(array[0][2])
		method = "backwards diagonal"

	#the line below is for debugging the winner list
	#print "This is the final winner list: -->", winner 

	#check len of winner list to make sure only one winner
	if len(winner) > 1:
		#return "Sorry, there was more than one winner. THIS CANNOT BE!"
		return 0
	elif len(winner) == 0:
		#return "Sorry, there was no winner"
		return 0
	else:
		#return "%s is the winner by %s" % (winner[0], method)
		return winner[0]

tttdraw()