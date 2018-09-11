
if __name__ == '__main__':

    testCase1 = [[1,2,7,3],[5,6,11,4],[9,10,15,8],[13,14,12,0]]
    testCase2 = [[5,1,7,3],[9,2,11,4],[13,6,15,8],[0,10,14,12]]
	fringe = []

	filename = input("Please enter the filename of the puzzle you wish to have solved...")
	# problem = readInFile(filename)
	tree = Tree()
	answer = tree.treeSearch(testCase1, fringe)
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

class Node:
	def __init__(self, problem, nodeId, head):
		self.nodeId = nodeId
		self.state = problem
		self.head = head
		self.tail = None

class Tree:
	def __init__(self):
		self.root = None

	def treeSearch(problem, fringe):
		#create the Node and Tree
		node = Node(problem, 0, None)
		#insert the node into the fringe
		fringe = insert(node, fringe);
		while(fringe != []):
			node = pop(fringe)
			if(goalTest(problem, state(node))):
				return node
			fringe = insertAll(expand(node, problem), fringe)
		return -1;

	#inserts into tree
	def insert(node, fringe):


	#nodes should contain a nodeId, state(problem), a head, and branches
	def makeNode(problem, nodeId):
		node = {}
		node['nodeId'] = nodeId
		node['state'] = problem
		node['head'] = 


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
