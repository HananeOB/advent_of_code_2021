def scanFile(input) :
	with open(input, 'r') as input:
		return input.readlines()


def task1(input) : 
	n = len(input)
	input = [ map(int, list(i.replace("\n", ""))) for i in input]
	gamma = ""
	epsilon = ""
	for l in list(zip(*input)) :
		if sum(l) >= (n//2) : 
			gamma += "1"
			epsilon += "0"
		else :
			gamma += "0"
			epsilon += "1"

	gamma = int(gamma, 2)
	epsilon = int(epsilon, 2)
	print(gamma, epsilon)
	return gamma * epsilon

def big_bit_criteria(input, i):
	if 2 * sum([ int(l[i]) for l in input]) >= len(input) :
		return [l for l in input if l[i] == "1"]
	else :
		return [l for l in input if l[i] == "0"]

def small_bit_criteria(input, i):
	if 2 * sum([ int(l[i]) for l in input]) < len(input) :
		return [l for l in input if l[i] == "1"]
	else :
		return [l for l in input if l[i] == "0"]

def task2(input) :
	O2 = [  list(i.replace("\n", "")) for i in input]
	CO2 = [  list(i.replace("\n", "")) for i in input]
	i = 0 

	while len(O2)>1:
		O2 = big_bit_criteria(O2,i)
		i += 1 
	i = 0
	while len(CO2)>1:
		CO2 = small_bit_criteria(CO2,i)
		i += 1 
	
	return int("".join(CO2[0]), 2) * int("".join(O2[0]), 2)
	 

if __name__ == "__main__" :
	print("Part 1 test result is ---> ", task1(scanFile("test.txt")))
	print("Part 1 result is ---> ", task1(scanFile("input.txt")))

	print("Part 2 test result is ---> ", task2(scanFile("test.txt")))
	print("Part 2 result is ---> ", task2(scanFile("input.txt")))

