#TODO: make difficulties, figure out how to nopt use global 
# choose x, 0


def printBoard(b):
	sep = " __|_|__"
	print("  1 2 3")
	print("A " + b[0]+"|" + b[1] + "|" + b[2])
	print (sep)
	print("B " + b[3]+"|" + b[4] + "|" + b[5])
	print (sep)
	print("C " + b[6]+"|" + b[7] + "|" + b[8])
	print("   | |")

def playAI(b,d):
	if d == 1:
		badAI(b)
	if d == 2:
		easyAI(b)
	if d == 3:
		hardAI(b)

def badAI(b):
	pass
def easyAI(b):
	pass

def hardAI(b):
	if win(b):
		pass
	elif block(b):
		pass
	#elif fork(b):
	#	pass
	elif blockFork(b):
		pass
	elif center(b):
		pass
	elif oppCorner(b):
		pass
	elif emptyCorner(b):
		pass
	elif emptySide(b):
		pass

def win(b):
	for i in range(0,len(b),3):
		if b[i] == "O" and b[i+1] == "O" and b[i+2] == " ":
			b[i+2] = "O"
			return True
		if b[i] == "O" and b[i+1] == " " and b[i+2] == "O":
			b[i+1] = "O"
			return True
		if b[i] == "O" and b[i+1] == "O" and b[i+2] == "O":
			b[i] = "O"
			return True
	for i in range(3):
		if b[i] == "O" and b[i+3] == "O" and b[i+6] == " ":
			b[i+6] = "O"
			return True
		if b[i] == "O" and b[i+3] == " " and b[i+6] == "O":
			b[i+3] = "O"
			return True
		if b[i] == " " and b[i+3] == "O" and b[i+6] == "O":
			b[i] = "O"
			return True
	if b[0] == "O" and b[4] == "O" and b[8] == " ":
		b[8] = "O"
		return True
	if b[0] == "O" and b[4] == " " and b[8] == "O":
		b[4] = "O"
		return True
	if b[0] == " " and b[4] == "O" and b[8] == "O":
		b[0] = "O"
		return True
	if b[2] == "O" and b[4] == "O" and b[6] == " ":
		b[6] = "O"
		return True
	if b[2] == "O" and b[4] == " " and b[6] == "O":
		b[4] = "O"
		return True
	if b[2] == " " and b[4] == "O" and b[6] == "O":
		b[2] = "O"
		return True
	return False

def block(b):
	for i in range(0,len(b),3):
		if b[i] == "X" and b[i+1] == "X" and b[i+2] == " ":
			b[i+2] = "O"
			return True
		if b[i] == "X" and b[i+1] == " " and b[i+2] == "X":
			b[i+1] = "O"
			return True
		if b[i] == "O" and b[i+1] == "X" and b[i+2] == "X":
			b[i] = "O"
			return True
	for i in range(3):
		if b[i] == "X" and b[i+3] == "X" and b[i+6] == " ":
			b[i+6] = "O"
			return True
		if b[i] == "X" and b[i+3] == " " and b[i+6] == "X":
			b[i+3] = "O"
			return True
		if b[i] == " " and b[i+3] == "X" and b[i+6] == "X":
			b[i] = "O"
			return True
	if b[0] == "X" and b[4] == "X" and b[8] == " ":
		b[8] = "O"
		return True
	if b[0] == "X" and b[4] == " " and b[8] == "X":
		b[4] = "O"
		return True
	if b[0] == " " and b[4] == "X" and b[8] == "X":
		b[0] = "O"
		return True
	if b[2] == "X" and b[4] == "X" and b[6] == " ":
		b[6] = "O"
		return True
	if b[2] == "X" and b[4] == " " and b[6] == "X":
		b[4] = "O"
		return True
	if b[2] == " " and b[4] == "X" and b[6] == "X":
		b[2] = "O"
		return True
	return False

def fork(b):
	count = 0
	for i in range(0,9,3):
		if b[i] != "X" and b[i+1] != "X" and b[i+2] != "X":
			count += 1
	for i in range(3):
		if b[i] != "X" and b[i+3] != "X" and b[i+6] != "X":
			count += 1
		if b[0] != "X" and b[4] != "X" and b[8] != "X":
	 		count += 1
		if b[2] != "X" and b[4] != "X" and b[6] != "X":
	 		count += 1

		if count == 2:
			return True
		#play in intersection of two lines
	return False


def blockFork(b):
	return False

def center(b):
	if b[4] != " ":
		return False
	b[4] = "O"
	return True

def oppCorner(b):
	if b[0] == "X" and b[8] == " ":
		b[8] = "O"
		return True
	elif b[2] == "X" and b[6] == " ":
		b[6] = "O"
		return True
	elif b[8] == "X" and b[0] == " ":
		b[0] = "O"
		return True
	elif b[6] == "X" and b[2] == " ":
		b[2] = "O"
		return True
	return False

def emptyCorner(b):
	if b[0] == " ":
		b[0] = "O"
		return True
	if b[2] == " ":
		b[2] = "O"
		return True
	if b[6] == " ":
		b[6] = "O"
		return True
	if b[8] == " ":
		b[8] = "O"
		return True
	return False

def emptySide(b):
	if b[1] == " ":
		b[1] = "O"
		return True
	if b[3] == " ":
		b[3] = "O"
		return True
	if b[5] == " ":
		b[5] = "O"
		return True
	if b[7] == " ":
		b[7] = "O"
		return True
	return False




def gameOver(b):
	
	if checkHorizontal(b) != " ":
		return checkHorizontal(b)
	if checkVertical(b) != " ":
		return checkVertical(b)
	if checkDiagonal(b) != " ":
		return checkDiagonal(b)
	if checkFull(b):
		return "Nobody"
	return " "

def checkHorizontal(b):
	if b[0] == b[1] == b[2]:
		if b[0] != " ":
			return b[0]
	if b[3] == b[4] == b[5]:
		if b[3] != " ":
			return b[3]
	if b[6] == b[7] == b[8]:
		if b[6] != " ":
			return b[6]
	return " "

def checkVertical(b):
	if b[0] == b[3] == b[6]:
		if b[0] != " ":
			return b[0]
	if b[1] == b[4] == b[7]:
		if b[1] != " ":
			return b[1]
	if b[2] == b[5] == b[8]:
		if b[2] != " ":
			return b[2]
	return " "

def checkDiagonal(b):
	if b[0] == b[4] == b[8]:
		if b[0] != " ":
			return b[0]
	if b[2] == b[4] == b[6]:
		if b[2] != " ":
			return b[2]
	return " "

def checkFull(b):
	for i in b:
		if i == " ":
			return False
	return True

def game():
	b = [" "]*9
	playerWin = False
	AIWin = False
	print("Welcome to Tic-Tac-Toe!")
	print()
	while gameOver(b) == " ":
		printBoard(b)
		print()
		print("Please enter COLUMN,ROW")
		c,r = input().split(",")
		if c == "A":
			b[int(r)-1] = "X"
		elif c == "B":
			b[3+ int(r)-1] = "X"
		elif c == "C":
			b[6+ int(r)-1] = "X"
		printBoard(b)
		hardAI(b)
	
game()
