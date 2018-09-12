class Node:
	def __init__(self, problem, head, depth):
		self.state = problem
		self.head = head
		self.depth = depth
		self.tails = []

class Tree:
	def __init__(self):
		self.root = None

	def iterativeDeepeningSearch(self, problem, goal):
		limit = 0
		#constantly loop until solution is found
		while(1):
			result = self.depthLimitedSearch(problem, goal, limit)
			limit += 1
			#this is the check for node otherwise continue
			if(result != 0 and result != True):
				return result
			#check to see if cutoff is hit
			elif(result == True):
				return -1


	def depthLimitedSearch(self, problem, goal, limit):
		node = Node(problem, None, 0)
		return self.recursiveDLS(node, problem, goal, limit)

	def recursiveDLS(self, node, problem, goal, limit):
		self.printNode(node);
		cutoff = f=False
		if(self.goalTest(goal, node.state)):
			return node
		elif(node.depth is limit):
			return cutoff
		else:
			for successor in self.expand(node.state, node, problem):
				result = self.recursiveDLS(successor, problem, goal, limit)
				if(result is cutoff):
					cutoff = True
				elif(result != failure):
					return result
			if(cutoff is True):
				return cutoff
			else:
				return failure

	def goalTest(self, goal, state):
		#traverse the 4x4 dict to check to see if the state matches the problem
		for x in range(0,4):
			for y in range(0,4):
				if(state[x][y] != goal[x][y]):
					return False
		return True;

	#expands the tree so it can send back a nodeList to insert into the fringe
	#this is the real logic behind the IDS
	def expand(self, puzzle_node, prevNode, problem):

	    expanded_nodes = []
	    i = 0
	    # Search for the empty space
	    while 0 not in puzzle_node[i]:
	        i += 1
	    # Record the column index of the empty space
	    j = puzzle_node[i].index(0)

	    #### Creating the possible states ####
	    # If the empty space is in the top three rows,
	    # add a node that represents moving the empty space down
	    if i < 3:
	        puzzle_node[i][j], puzzle_node[i+1][j] = puzzle_node[i+1][j], puzzle_node[i][j]
	        expanded_nodes.append(puzzle_node)
	        puzzle_node[i][j], puzzle_node[i+1][j] = puzzle_node[i+1][j], puzzle_node[i][j]

	    # If the empty space is in the bottom 3 rows,
	    # add a node that represents moving the empty space up
	    if i > 0:
	        puzzle_node[i][j], puzzle_node[i-1][j] = puzzle_node[i-1][j], puzzle_node[i][j]
	        expanded_nodes.append(puzzle_node)
	        puzzle_node[i][j], puzzle_node[i-1][j] = puzzle_node[i-1][j], puzzle_node[i][j]

	    # If the empty space is in the left three columns,
	    # add a node that represents the empty space moving to the right
	    if j < 3:
	        puzzle_node[i][j], puzzle_node[i1][j+1] = puzzle_node[i][j+1], puzzle_node[i][j]
	        expanded_nodes.append(puzzle_node)
	        puzzle_node[i][j], puzzle_node[i][j+1] = puzzle_node[i][j+1], puzzle_node[i][j]

	    # If the empty space is in the right three columns,
	    # add a node that represents the empty space moving to the left
	    if j < 3:
	        puzzle_node[i][j], puzzle_node[i1][j-1] = puzzle_node[i][j-1], puzzle_node[i][j]
	        expanded_nodes.append(puzzle_node)
	        puzzle_node[i][j], puzzle_node[i][j-1] = puzzle_node[i][j-1], puzzle_node[i][j]

	    #added during OO implementation to make it easier to work with the tree
	    nodeList = []
	    for x in expanded_nodes:
	    	depth = prevNode.depth + 1
	    	n = Node(x, prevNode, depth)
	    	nodeList.append(n)
	    return nodeList

	def printNode(self, node):
		for x in range(0,4):
			for y in range(0,4):
				if(node.state[x][y] <= 9):
					print("0", end='')
				print(node.state[x][y], end='')
				print(" ", end='')
			print("\n", end='') 
		print("--------------------")


if __name__ == '__main__':
    testCase1 = [[1,2,7,3],[5,6,11,4],[9,10,15,8],[13,14,12,0]]
    testCase2 = [[5,1,7,3],[9,2,11,4],[13,6,15,8],[0,10,14,12]]
    goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    fringe = []
    #filename = input("Please enter the filename of the puzzle you wish to have solved...")
    # problem = readInFile(filename)
    tree = Tree()
    answer = tree.iterativeDeepeningSearch(testCase1, goal)
    if(answer is -1):
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

	# def treeSearch(problem, fringe, goal):
	# 	#create the root node
	# 	node = Node(problem, 0, None)
	# 	#insert the root node into the fringe
	# 	fringe.append(node)
	# 	#loop thru fringe till it is empty or the fringe reaches 1,000,000 nodes per assignment requirements
	# 	while(fringe not [] || len(fringe) < 1000000):
	# 		#DFS is a LIFO operation
	# 		node = pop(fringe)
	# 		#check goal vs node on fringe
	# 		if(goalTest(goal, node.state)):
	# 			return node
	# 		fringe = insertAll(expand(node, problem), fringe)
	# 	return -1;

	# #simple pop function for returning node off a stack
	# def pop(fringe):
	# 	if fringe not []:
	# 		return fringe.pop(-1)
	# 	else:
	# 		return -1


	# #inserts all nodes given into the fringe dict
	# def insertAll(nodeList, fringe):

