BOARD_DIM = 6
EMPTY_CHAR = 'E'

"""
CASE NUMBERS
0: No moves
1: two-side-open-3-in-a-row
2: one-side-3-in-a-row
3: open-2-in-a-row
"""


# Checks spaces that are above and below the given space
# Returns the appropriate case number and sorted coordinates of the case
def check_vertical(x, y, board, player_char, opp_char):

	coordinate_list = [(x,y)]

	vertical_char_count = 1
	empty_space_count = 0

	j = y
	# Checking Upward
	while(j != 0):
		current_char = board[x][j-1]

		if current_char == player_char:
			vertical_char_count += 1
			j-=1
			coordinate_list.append((x,j))
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Checking Downward
	j = y
	while(j != BOARD_DIM-1):
		current_char = board[x][j+1]

		if current_char == player_char:
			vertical_char_count += 1
			coordinate_list.append((x,j))
			j+=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Returning the appropriate case numbers and coordinate_list

	# Sort the list by the x coordinate
	coordinate_list = sorted(coordinate_list, key=lambda coord: coord[0])
	# print(vertical_char_count)
	# print(empty_space_count)
	if vertical_char_count <= 1 or empty_space_count == 0:
		# print(1)
		coordinate_list = []
		# print('return')
		return 0, coordinate_list

	elif vertical_char_count == 2:
		# print('return')
		return 3, coordinate_list

	elif vertical_char_count == 3 or vertical_char_count >= 4:
		if empty_space_count == 1 and vertical_char_count < 4:
			# print('return')
			return 2, coordinate_list
		elif empty_space_count == 2 or vertical_char_count >= 4:
			# print('return')
			return 1, coordinate_list

def check_horizontal(x, y, board, player_char, opp_char):

	coordinate_list = [(x,y)]

	horizontal_char_count = 1
	empty_space_count = 0

	# Checking Left
	i = x

	while(i != 0):
		current_char = board[i-1][y]

		if current_char == player_char:
			horizontal_char_count += 1
			coordinate_list.append((i,y))
			i -= 1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Checking Right
	i = x
	while(i != BOARD_DIM-1):
		current_char = board[i+1][y]

		if current_char == player_char:
			horizontal_char_count += 1
			coordinate_list.append((i,y))
			i += 1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Returning the appropriate case numbers and coordinate_list
	coordinate_list = sorted(coordinate_list, key=lambda coord: coord[0])

	if horizontal_char_count <= 1 or empty_space_count == 0:
		coordinate_list = []
		return 0, coordinate_list

	elif horizontal_char_count == 2:
		return 3, coordinate_list

	elif horizontal_char_count == 3 or horizontal_char_count >= 4:
		if empty_space_count == 1 and horizontal_char_count < 4:
			return 2, coordinate_list
		elif empty_space_count == 2 or horizontal_char_count >= 4:
			return 1, coordinate_list

def check_diagonal_down(x, y, board, player_char, opp_char):

	coordinate_list = [(x,y)]

	diagonal_char_count = 1
	empty_space_count = 0

	# Checking Left and Up
	i, j = x, y
	while(i != 0 and j != 0):

		current_char = board[i-1][j-1]

		if current_char == player_char:
			diagonal_char_count += 1
			coordinate_list.append((i,j))
			i-=1
			j-=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Checking Right and Down
	i, j = x, y
	while(i != BOARD_DIM-1 and j != BOARD_DIM-1):

		current_char = board[i+1][j+1]

		if current_char == player_char:
			diagonal_char_count += 1
			coordinate_list.append((i,j))
			i+=1
			j+=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break


	# Returning the appropriate case numbers and coordinate_list
	coordinate_list = sorted(coordinate_list, key=lambda coord: coord[0])

	if diagonal_char_count <= 1 or empty_space_count == 0:
		coordinate_list = []
		return 0, coordinate_list

	elif diagonal_char_count == 2:
		return 3, coordinate_list

	elif diagonal_char_count == 3 or diagonal_char_count >= 4:
		if empty_space_count == 1 and diagonal_char_count < 4:
			return 2, coordinate_list
		elif empty_space_count == 2 or diagonal_char_count >= 4:
			return 1, coordinate_list


def check_diagonal_up(x, y, board, player_char, opp_char):

	coordinate_list = [(x,y)]
	diagonal_char_count = 1
	empty_space_count = 0

	# LEFT AND DOWN
	i, j = x, y

	while(j != BOARD_DIM-1 and i != 0):

		current_char = board[i-1][j+1]

		if current_char == player_char:
			diagonal_char_count += 1
			coordinate_list.append((i,j))
			i-=1
			j+=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Checking Right and Up
	i, j = x,y

	while(j != 0 and i != BOARD_DIM-1):

		current_char = board[i+1][j-1]

		if current_char == player_char:
			diagonal_char_count += 1
			coordinate_list.append((i,j))
			i+=1
			j-=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Returning the appropriate case numbers and coordinate_list
	coordinate_list = sorted(coordinate_list, key=lambda coord: coord[0])

	if diagonal_char_count <= 1 or empty_space_count == 0:
		coordinate_list = []
		return 0, coordinate_list

	elif diagonal_char_count == 2:
		return 3, coordinate_list

	elif diagonal_char_count == 3 or diagonal_char_count >= 4:
		if empty_space_count == 1 and diagonal_char_count < 4:
			return 2, coordinate_list
		elif empty_space_count == 2 or diagonal_char_count >= 4:
			return 1, coordinate_list

def populate_lists(x,y, board, player_char, opp_char, three_two_open, three_one_open, two_open, check_function):
	case, coordinates = check_function(x, y, board, player_char, opp_char)
	if coordinates:
		if case == 1:
			if coordinates not in three_two_open:
				three_two_open.append(coordinates)

		elif case == 2:
			if coordinates not in three_one_open:
				three_one_open.append(coordinates)

		elif case == 3:
			if coordinates not in two_open:
				two_open.append(coordinates)

def heuristic(x, y, board, player_char, opp_char):
	player_three_two_open = []
	player_three_one_open = []
	player_two_open = []

	opponent_three_two_open = []
	opponent_three_one_open = []
	opponent_two_open = []

	for i in range(BOARD_DIM):
		for j in range(BOARD_DIM):

			if board[i][j] == EMPTY_CHAR:
				continue

			elif board[i][j] == player_char:
				# Vertical Check
				populate_lists(i, j, board, player_char, opp_char, player_three_two_open, player_three_one_open, player_two_open, check_vertical)
				# Horizontal Check
				populate_lists(i, j, board, player_char, opp_char, player_three_two_open, player_three_one_open, player_two_open, check_horizontal)
				# Check Diagonal
				populate_lists(i, j, board, player_char, opp_char, player_three_two_open, player_three_one_open, player_two_open, check_diagonal_up)
				populate_lists(i, j, board, player_char, opp_char, player_three_two_open, player_three_one_open, player_two_open, check_diagonal_down)

			elif board[i][j] == opp_char:
				# Vertical Check
				populate_lists(i, j, board, opp_char, player_char, opponent_three_two_open, opponent_three_one_open, opponent_two_open, check_vertical)
				# Horizontal Check
				populate_lists(i, j, board, opp_char, player_char, opponent_three_two_open, opponent_three_one_open, opponent_two_open, check_horizontal)
				# Check Diagonal
				populate_lists(i, j, board, opp_char, player_char, opponent_three_two_open, opponent_three_one_open, opponent_two_open, check_diagonal_up)
				populate_lists(i, j, board, opp_char, player_char, opponent_three_two_open, opponent_three_one_open, opponent_two_open, check_diagonal_down)




	p_tto = len(player_three_two_open)
	p_too = len(player_three_one_open)
	p_to = len(player_two_open)

	o_tto = len(opponent_three_two_open)
	o_too = len(opponent_three_one_open)
	o_to = len(opponent_two_open)

	heuristic = (5 * p_tto) - (10 * o_tto) + (3 * p_too) - (6 * o_too) + p_to - o_to

	return heuristic
