import copy
import time

class Node:
	def __init__(self, problem, head, depth):
		self.count = 0
		self.state = problem
		self.head = head
		self.depth = depth
		self.tails = []

class Result:
	def __init__(self, value, count, solution):
		self.value = value
		self.count = count
		self.solution = solution

class Tree:
	def __init__(self):
		self.root = None

	def iterativeDeepeningSearch(self, problem, goal):
		limit = 0
		result = Result(-1, 0, problem)
		#constantly loop until solution is found
		while(1):
			# print("while loop")
			result = self.depthLimitedSearch(problem, goal, limit)
			limit += 1
			#this is the check for node otherwise continue
			return result



	def depthLimitedSearch(self, problem, goal, limit):
		node = Node(problem, None, 0)
		return self.recursiveDLS(node, 0, problem, goal, limit)

	def recursiveDLS(self, node, count, problem, goal, limit):
		result = Result(5, count, node)
		# if(node.depth % 15 == 0):
		# print("depth: ", end='')
		# print(node.depth)
		# self.printNode(node)
		cutoff = False
		if(self.goalTest(goal, node.state)):
			result.value = 1
			result.solution = node
			# result.count = count
			return result
		elif(node.depth is limit):
			result.value = 0
			result.solution = node
			# result.count = count
			return result
		else:
			nodeList = self.expand(node.state, node, problem)
			result.count += len(nodeList)
			for successor in nodeList:
				result = self.recursiveDLS(successor, result.count, problem, goal, limit)
				if(result.value == 0):
					cutoff = True
				elif(result.value != -1):
					return result
			if(cutoff is True):
				result.value = 0
				return result
			else:
				result.value = -1
				return result

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
		# print("Entered expand")
		expanded_nodes = []
		i = 0
		while 0 not in puzzle_node[i]:
			i += 1
		j = puzzle_node[i].index(0)
		# print(i)
		# print(j)
		if i < 3:
			puzzle_node[i][j], puzzle_node[i+1][j] = puzzle_node[i+1][j], puzzle_node[i][j]
			# print(puzzle_node[i][j])
			# print(puzzle_node[i+1][j])
			expanded_nodes.append(copy.deepcopy(puzzle_node))
			puzzle_node[i][j], puzzle_node[i+1][j] = puzzle_node[i+1][j], puzzle_node[i][j]

		if i > 0:
			puzzle_node[i][j], puzzle_node[i-1][j] = puzzle_node[i-1][j], puzzle_node[i][j]
			# print(puzzle_node[i][j])
			# print(puzzle_node[i-1][j])
			expanded_nodes.append(copy.deepcopy(puzzle_node))
			puzzle_node[i][j], puzzle_node[i-1][j] = puzzle_node[i-1][j], puzzle_node[i][j]

		if j < 3:
			puzzle_node[i][j], puzzle_node[i][j+1] = puzzle_node[i][j+1], puzzle_node[i][j]
			# print(puzzle_node[i][j])
			# print(puzzle_node[i][j+1])
			expanded_nodes.append(copy.deepcopy(puzzle_node))
			puzzle_node[i][j], puzzle_node[i][j+1] = puzzle_node[i][j+1], puzzle_node[i][j]

		if j > 0:
			puzzle_node[i][j], puzzle_node[i][j-1] = puzzle_node[i][j-1], puzzle_node[i][j]
			# print(puzzle_node[i][j])
			# print(puzzle_node[i][j-1])
			expanded_nodes.append(copy.deepcopy(puzzle_node))
			puzzle_node[i][j], puzzle_node[i][j-1] = puzzle_node[i][j-1], puzzle_node[i][j]

		# for d in expanded_nodes:
		# 	for x in range(0,4):
		# 		for y in range(0,4):
		# 			if(d[x][y] <= 9):
		# 				print("0", end='')
		# 			print(d[x][y], end='')
		# 			print(" ", end='')
		# 		print("\n", end='') 
		# 	print("--------------------")

		nodeList = []
		for x in expanded_nodes:
			depth = prevNode.depth + 1
			n = Node(x, prevNode, depth)
			# self.printNode(n)
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
	start_time = time.process_time()
	testCase1 = [[1,2,7,3],[5,6,11,4],[9,10,15,8],[13,14,12,0]]
	testCase2 = [[5,1,7,3],[9,2,11,4],[13,6,15,8],[0,10,14,12]]
	testCase3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,0,14,15]]
	testCase4 = [[1,2,3,4],[5,6,7,8],[0,10,11,12],[9,13,14,15]]
	testCase5 = [[1,2,3,4],[5,6,7,0],[9,10,11,8],[13,14,15,12]]
	testCase6 = [[1,2,3,4],[5,6,7,8],[9,10,11,0],[13,14,15,12]]
	goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
	tree = Tree()
	result = Result(-1, 0, testCase1)
	result = tree.iterativeDeepeningSearch(testCase1, goal)
	# tree.printNode(result.solution)
	end_time = time.process_time()
	if(result.value is -1):
		print(end_time - start_time)
		print("Life is hard and the program failed. Sorry...")
	elif(result.value is -2):
		print(end_time - start_time)
		print("Reached 1000000 nodes!")
	else:
		print(result.count)
		tree.printNode(result.solution)
		print(end_time - start_time)
		print("Life is good! The program worked!")
