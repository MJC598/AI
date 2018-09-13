from queue import PriorityQueue
from copy import deepcopy

def get_manhattan_distance(puzzle_node):

	manhattan_distance = 0

	for i in range(4):
		for j in range(4):

			number = puzzle_node[i][j]
			if number != i * 4 + (j+i) and number != 0:
				correct_i = (number - 1) // 4
				correct_j = (number - 1) % 4
				manhattan_distance += abs(i - correct_i) + abs(j - correct_j)

	return manhattan_distance

def expand_node(puzzle_node):

	expanded_nodes = []

	i = 0
	# Search for the empty space
	while 0 not in puzzle_node[i]: i += 1
	j = puzzle_node[i].index(0)

	# Search for the empty space
	while 0 not in puzzle_node[i]:
		i += 1
	j = puzzle_node[i].index(0)

	#### Creating the possible states ####

	# If the empty space is in the top three rows,
	# add a node that represents moving the empty space down
	if i < 3:
		puzzle_node[i][j], puzzle_node[i+1][j] = puzzle_node[i+1][j], puzzle_node[i][j]
		expanded_nodes.append((deepcopy(puzzle_node), "D"))
		puzzle_node[i][j], puzzle_node[i+1][j] = puzzle_node[i+1][j], puzzle_node[i][j]

	# If the empty space is in the bottom 3 rows,
	# add a node that represents moving the empty space up
	if i > 0:
		puzzle_node[i][j], puzzle_node[i-1][j] = puzzle_node[i-1][j], puzzle_node[i][j]
		expanded_nodes.append((deepcopy(puzzle_node), "U"))
		puzzle_node[i][j], puzzle_node[i-1][j] = puzzle_node[i-1][j], puzzle_node[i][j]

	# If the empty space is in the left three columns,
	# add a node that represents the empty space moving to the right

	if j < 3:
		puzzle_node[i][j], puzzle_node[i][j+1] = puzzle_node[i][j+1], puzzle_node[i][j]
		expanded_nodes.append((deepcopy(puzzle_node), "R"))
		puzzle_node[i][j], puzzle_node[i][j+1] = puzzle_node[i][j+1], puzzle_node[i][j]

	# If the empty space is in the right three columns,
	# add a node that represents the empty space moving to the left
	if j > 0:
		puzzle_node[i][j], puzzle_node[i][j-1] = puzzle_node[i][j-1], puzzle_node[i][j]
		expanded_nodes.append((deepcopy(puzzle_node), "L"))
		puzzle_node[i][j], puzzle_node[i][j-1] = puzzle_node[i][j-1], puzzle_node[i][j]

	return expanded_nodes

def create_tuple(puzzle_node):
	return tuple([num for row in puzzle_node for num in row])

def astar(puzzle_node, solution):

	fringe = PriorityQueue()
	visited_nodes = set()
	answer = ""
	expanded_count = 0

	## FORMAT: (total manhattan distance, level, the current state, the current answer)
	fringe.put((0, 0, puzzle_node, ""))

	while not fringe.empty():

		_, level, current_state, current_answer = fringe.get()

		if expanded_count > 1000000:
			break

		done = True

		for i in range(4):
			for j in range(1, 5):
				if current_state[i][j-1] != i * 4 + j and (i != 3 or j != 4):
					done = False
		if(done):
			answer = current_answer
			print("Expanded Count: ", expanded_count)
			return answer

		expanded_nodes = expand_node(current_state)

		for node, instruction in expanded_nodes:
			node_tuple = create_tuple(node)

			if node_tuple not in visited_nodes:
				manhattan_distance = get_manhattan_distance(node)
				visited_nodes.add(node_tuple)

				fringe.put((manhattan_distance + level + 1 , level+1, node, current_answer+instruction))
		expanded_count += 1

def print_node(puzzle_node):
	for x in range(0,4):
		for y in range(0,4):
			if(puzzle_node[x][y] <= 9):
				print("0", end='')
			print(puzzle_node[x][y], end='')
			print(" ", end='')
		print("\n", end='')
	print("--------------------")


def print_solution(puzzle_node, solution_sequence):

	sequence_count = 0
	print_node(puzzle_node)

	for l in range(len(solution_sequence)):

		instruction = solution_sequence[l]

		i = 0
		# Search for the empty space
		while 0 not in puzzle_node[i]: i += 1
		j = puzzle_node[i].index(0)

		if instruction == 'D':
			puzzle_node[i][j], puzzle_node[i+1][j] = puzzle_node[i+1][j], puzzle_node[i][j]
			print_node(puzzle_node)
			sequence_count += 1

		elif instruction == 'U':
			puzzle_node[i][j], puzzle_node[i-1][j] = puzzle_node[i-1][j], puzzle_node[i][j]
			print_node(puzzle_node)
			sequence_count += 1

		elif instruction == 'R':
			puzzle_node[i][j], puzzle_node[i][j+1] = puzzle_node[i][j+1], puzzle_node[i][j]
			print_node(puzzle_node)
			sequence_count += 1

		elif instruction == 'L':
			puzzle_node[i][j], puzzle_node[i][j-1] = puzzle_node[i][j-1], puzzle_node[i][j]
			print_node(puzzle_node)
			sequence_count += 1


	print("Solution found in " , sequence_count, "Steps!")

if __name__ == '__main__':

	test_case_1 = [[1,2,7,3],[5,6,11,4],[9,10,15,8],[13,14,12,0]]
	test_case_2 = [[5,1,7,3],[9,2,11,4],[13,6,15,8],[0,10,14,12]]
	solution = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]

	solution_sequence_1 = astar(test_case_1, solution)
	print_solution(test_case_1, solution_sequence_1)
	print("Solution Sequence: ", solution_sequence_1)

	solution_sequence_2 = astar(test_case_2, solution)
	print_solution(test_case_2, solution_sequence_2)
	print("Solution Sequence: ", solution_sequence_2)
