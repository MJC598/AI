import copy
import datetime

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

class Graph:
	def __init__(self):
		self.root = None

	def graph_search(self, problem, fringe, goal):
		closed = []
		result = Result(-1, 0, problem)
		node = Node(problem, None, 0)
		fringe = [node]
		while(len(fringe) <= 1000000):
			if(fringe == []):
				result.value = -1
				return result
			node = fringe.pop(0)
			# self.printNode(node)
			if(self.goalTest(goal, node.state)):
				result.solution = node
				result.value = 0
				return result
			if node not in closed:
				closed.append(node)
				nodeList = self.expand(node.state, node, problem)
				result.count += len(nodeList)
				if(result.count <= 5):
					for x in nodeList:
						self.printNode(x)
				# if(result.count % 1000 == 0):
				# 	print(result.count)
				if(result.count >= 1000000):
					result.value = -2
					return result
				for x in nodeList:
					fringe.append(x)


	def goalTest(self, goal, state):
	#traverse the 4x4 dict to check to see if the state matches the problem
		for x in range(0,4):
			for y in range(0,4):
				if(state[x][y] != goal[x][y]):
					return False
		return True;

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
	start_time = datetime.datetime.now()
	testCase1 = [[1,2,7,3],[5,6,11,4],[9,10,15,8],[13,14,12,0]]
	testCase2 = [[5,1,7,3],[9,2,11,4],[13,6,15,8],[0,10,14,12]]
	testCase3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,0,14,15]]
	testCase4 = [[1,2,3,4],[5,6,7,8],[0,10,11,12],[9,13,14,15]]
	goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
	fringe = []
	#filename = input("Please enter the filename of the puzzle you wish to have solved...")
	# problem = readInFile(filename)
	graph = Graph() 
	result = Result(-1, 0, testCase1)
	result = graph.graph_search(testCase2, fringe, goal)
	end_time = datetime.datetime.now()
	ctime = end_time - start_time
	if(result.value is -1):
		print(ctime.microseconds, end='')
		print(" microseconds")
		print("Life is hard and the program failed. Sorry...")
	elif(result.value is -2):
		print(result.count)
		print(ctime.microseconds, end='')
		print(" microseconds")
		print("Reached 1000000 nodes program was terminated!")
	else:
		x = 0
		depth = result.solution.depth
		print("Puzzle Steps From End to Beginning")
		graph.printNode(result.solution)
		while(x < depth):
			graph.printNode(result.solution.head)
			result.solution = copy.deepcopy(result.solution.head)
			x += 1
		print("nodes created: ", end='')
		print(result.count)
		print("time taken to execute: ", end='')
		print(ctime.microseconds, end='')
		print(" microseconds")
		print("Life is good! The program worked!")