def scanFile(input) :
	with open(input, 'r') as input:
		return input.readlines()


def task1(input) : 
	horizontal_moves = sum([ int(move.split(" ")[1]) for move in input if move.split(" ")[0] == "forward"])
	down_moves = sum([ int(move.split(" ")[1]) for move in input if move.split(" ")[0] == "down"])
	up_moves = sum([ -1 * int(move.split(" ")[1]) for move in input if move.split(" ")[0] == "up"])

	return horizontal_moves * (down_moves+up_moves)

def task2(input) :

	aim = 0
	horizontal_position = 0
	depth = 0
	for move in input :
		if move.split(" ")[0] == "forward" :
			horizontal_position += int(move.split(" ")[1])
			depth += aim * int(move.split(" ")[1])

		elif move.split(" ")[0] == "down" :
			aim += int(move.split(" ")[1])

		else :
			aim -= int(move.split(" ")[1])

	return horizontal_position*depth
		 

if __name__ == "__main__" :
	print("Part 1 test result is ---> ", task1(scanFile("test.txt")))
	print("Part 1 result is ---> ", task1(scanFile("input.txt")))

	print("Part 2 test result is ---> ", task2(scanFile("test.txt")))
	print("Part 2 result is ---> ", task2(scanFile("input.txt")))

# An improvement to solution code be replacing int(move.split(" ")[0]) by command