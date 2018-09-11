fringe = []
problem = [][]

filename = input("Please enter the filename of the puzzle you wish to have solved...")
problem = readInFile(filename)
answer = treeSearch(problem, fringe)
if(answer == -1):
	print("Life is hard and the program failed. Sorry...")
else:
	print("Life is good! The program worked!")


def readInFile(filename):
	problem = [][]
	with open(filename, 'r') as f:
		#so, theoretically, this loops thru trying to add values to problem[][] giving a 4x4 matrix
		for x in xrange(1,4):
			for y in xrange(1,4):
				problem[x][y] = f.read()
	return problem


def treeSearch(problem, fringe):
	fringe = insert(makeNode(initState[problem]), fringe);
	while(fringe != []):
		node = pop(fringe)
		if(goalTest(problem, state(node))):
			return node
		fringe = insertAll(expand(node, problem), fringe)
	return -1;

def insert():

def makeNode():