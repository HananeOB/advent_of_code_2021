# exo 1 

with open("1.input", 'r') as f: 
	numbers = [int(i) for i in  f.read().split('\n')]
n = len(numbers)
count = 0 
for i in range(1, n) :
	if numbers[i-1] < numbers[i] :
		count += 1 

print(count) 

# sliding windows 
window_length = 3 
count = 0 
new_numbers = [sum(numbers[i: i+window_length ]) for i in range(n-window_length+1)  ]
n = len(new_numbers)

for i in range(1, n) :
	if new_numbers[i-1] < new_numbers[i] :
		count += 1 


print(count)

l = ["hello", "Hii"]
m = ["dear", "lilo", 'nani']

print(list(zip(l,m)))
print(int(True))


# Write more intellignet and easy to read code 
# >>> write functions 
# Example of well written code : 

def scanFile(input):
    with open(input, "r") as input:
        return input.readlines()

def task1(input):
    return sum([int(i) < int(j) for i, j in zip(input, input[1:]) ] )

def task2(input):
    increased = 0

    for i in range(0, len(input)):

        firstBatch = input[i:i+3]
        secondBatch = input[i+1:i+4]

        if sum(map(int, firstBatch)) < sum(map(int, secondBatch)):
            increased +=1
    return increased

if __name__ == '__main__':
    print("Part 1 result is ---> ", task1(scanFile("input.txt")))
    print("Part 2 result is ---> ", task2(scanFile("input.txt")))