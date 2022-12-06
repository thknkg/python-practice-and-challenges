import re

instruction_set = []
shipping_containers = []
d = {}

for line in open("day_5.txt"):
	
	# only get instructions and reduce them down to lists of numbers
	if line.startswith("move"):
		div = [i.strip() for i in line.split(" ")]
		instruction_set.append([int(div[1]), int(div[3]), int(div[5])])
	
	# exclude numerical rows and only get rows with letters
	elif any(char.isdigit() for char in line) == False and any(char.isalpha() for char in line) == True:
		
		# sort by blocks of space (so that the empty spaces don't make things misaligned) and remove brackets/newlines
		edited_list = re.split(" {4}| ", re.sub("[\[\]\\n]+", "", line))
		shipping_containers.append(edited_list)
		
# get key value pairs where values are lists and keys are based on len of lists
d = {key:[] for key in range(0, len([[i for i in j] for j in shipping_containers]))}

# fill lists, excluding blank spots
for l in shipping_containers:
	for i in range(0, len(l)):
		if i not in d :	
			d[i] = []
	
		if l[i] != "":	
			d[i].append(l[i])

def move_containers(instruct):
	"""pop from one list and place at top of another"""
	for i in instruct:
		count, source, destination = i[0], i[1] - 1, i[2] - 1
		for i in range(0, count):
			d[destination].insert(0, d[source].pop(0))
	print(*[i[0] for i in d.values()])
	
def move_multiple_containers(instruct):
	"""pop multiple from one list and place at top of another"""
	for i in instruct:
		count, source, destination = i[0], i[1] - 1, i[2] - 1
		for i in range(0, count):
			if i == 0:
				d[destination].insert(0, d[source].pop(0))
				
			# position it in its previous relative location
			elif i < count:
				d[destination].insert(i, d[source].pop(0))
	
	print(*[i[0] for i in d.values()])
	
	
									
#move_containers(instruction_set)
move_multiple_containers(instruction_set)
