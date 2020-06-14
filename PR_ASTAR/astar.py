
import queue

#faalla
def laberinto():
	lab= [["#","#", "#", "#", "#", "O", "#", "#", "#"],
	["#"," ", " ", " ", " ", " ", " ", " ", "#"],
	["#"," ", "#", "#", " ", "#", "#", " ", "#"],
	["#"," ", "#", " ", " ", " ", "#", " ", "#"],
	["#"," ", "#", "X", "#", " ", "#", " ", "#"],
	["#"," ", "#", " ", "#", " ", "#", " ", "#"],
	["#"," ", "#", " ", "#", " ", "#", "#", "#"],
	["#"," ", " ", " ", " ", " ", " ", " ", "#"],
	["#","#", "#", "#", "#", "#", "#", "#", "#"]]

	return lab


def printlaberinto(laberinto, path=""):
	for x, pos in enumerate(laberinto[0]):
		if pos == "O":
			start = x

	i = start
	j = 0
	pos = set()
	for mov in path:
		if mov == "I":
			i -= 1

		elif mov == "D":
			i += 1

		elif mov == "Ar":
			j -= 1

		elif mov == "A":
			j += 1
		pos.add((j, i))

	for j, row in enumerate(laberinto):
		for i, col in enumerate(row):
			if (j, i) in pos:
				print("+ ", end="")
			else:
				print(col + " ", end="")
		print()
#---------------------------------------------------------------
def valid(laberinto, movimientos):
	for x, pos in enumerate(laberinto[0]):
		if pos == "O":
			start = x

	i = start
	j = 0
	for mov in movimientos:
		if mov == "I":
			i -= 1

		elif mov == "D":
			i += 1

		elif mov == "Ar":
			j -= 1

		elif mov == "A":
			j += 1

		if not(0 <= i < len(laberinto[0]) and 0 <= j < len(laberinto)):
			return False
		elif (laberinto[j][i] == "#"):
			return False

	return True
##_-------------------------------------------------------------------------------
def findEnd(laberinto, movimientos):
	for x, pos in enumerate(laberinto[0]):
		if pos == "O":
			start = x

	i = start
	j = 0
	for mov in movimientos:
		if mov == "I":
			i -= 1

		elif mov == "D":
			i += 1

		elif mov == "Ar":
			j -= 1

		elif mov == "A":
			j += 1

	if laberinto[j][i] == "X":
		print("Encontrado: " + movimientos)
		printlaberinto(laberinto, movimientos)
		return True

	return False


#_-----------------------------------------------------------------------

x = queue.Queue()
x.put("")
add = ""
laberinto  = Laberinto()

while not findEnd(laberinto, add): 
	add = x.get()
	#print(add)
	for j in ["I", "D", "Ar", "A"]:
		put = add + j
		if valid(laberinto, put):
			x.put(put)
