
if __name__ == '__main__':

    testCase1 = [[1,2,7,3],[5,6,11,4],[9,10,15,8],[13,14,12,0]]
    testCase2 = [[5,1,7,3],[9,2,11,4],[13,6,15,8],[0,10,14,12]]
	fringe = []

	filename = input("Please enter the filename of the puzzle you wish to have solved...")
	# problem = readInFile(filename)
	answer = treeSearch(testCase1, fringe)
	if(answer == -1):
		print("Life is hard and the program failed. Sorry...")
	else:
		print("Life is good! The program worked!")


# def readInFile(filename):
# 	problem = [][]
# 	with open(filename, 'r') as f:
# 		#so, theoretically, this loops thru trying to add values to problem[][] giving a 4x4 matrix
# 		for x in xrange(1,4):
# 			for y in xrange(1,4):
# 				problem[x][y] = f.read()
# 	return problem


def treeSearch(problem, fringe):
	fringe = insert(makeNode(problem), fringe);
	while(fringe != []):
		node = pop(fringe)
		if(goalTest(problem, state(node))):
			return node
		fringe = insertAll(expand(node, problem), fringe)
	return -1;

#inserts into tree
def insert(node, fringe):


#nodes should contain a nodeId, state(problem), a head, and branches
def makeNode(problem):


#simple pop function off a stack
def pop(fringe):
	if fringe not []:
		return fringe[0]
	else:
		return -1;

def goalTest(problem, state):
	#traverse the 4x4 dict to check to see if the state matches the problem
	for x in xrange(1,4):
		for y in xrange(1,4):
			if(state[x][y] != problem[x][y]):
				return false
	return true;

#returns state given a nodeId
def state(node):


#inserts all nodes given into the fringe dict
def insertAll(nodeList, fringe):


#expands the tree so it can send back a nodeList to insert into the fringe
def expand(node, problem):
