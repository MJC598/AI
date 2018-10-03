BOARD_DIM = 6
P1_CHAR = 'X'
P2_CHAR = 'O'
EMPTY_CHAR = 'E'

"""
CASE NUMBERS
0: No moves
1: two-side-open-3-in-a-row
2: one-side-3-in-a-row
3: open-2-in-a-row
"""


# Checks spaces that are above and below the given space
# Returns the appropriate case number
def check_vertical(x, y, board, player_char, opp_char):

	vertical_char_count = 1
	empty_space_count = 0

	j = y
	# Checking Upward
	while(j != 0):
		current_char = board[x][j-1]

		if current_char == player_char:
			vertical_char_count += 1
			j-=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break


	# Checking Downward
	j = y
	while(j != BOARD_DIM):
		current_char = board[x][j+1]

		if current_char == player_char:
			vertical_char_count += 1
			j+=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1

	# Returning the appropriate case numbers

	if vertical_char_count <= 1 or empty_space_count == 0:
		return 0

	elif vertical_char_count == 2:
		return 3

	elif vertical_char_count == 3:
		if empty_space_count == 1:
			return 2
		elif empty_space_count == 2:
			return 1

def check_horizontal(x, y, board, player_char, opp_char):

	horizontal_char_count = 1
	empty_space_count = 0

	# Checking Left
	i = x

	while(i != 0):
		current_char = board[i-1][j]

		if current_char == player_char:
			horizontal_char_count += 1
			i -= 1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	# Checking Right
	i = x
	while(i != BOARD_DIM):
		current_char = board[i+1][y]

		if current_char == player_char:
			horizontal_char_count += 1
			i += 1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break

	 # Returning the appropriate case numbers

	if horizontal_char_count <= 1 or empty_space_count == 0:
		return 0

	elif horizontal_char_count == 2:
		return 3

	elif horizontal_char_count == 3:
		if empty_space_count == 1:
			return 2
		elif empty_space_count == 2:
			return 1

def check_diagonal_down(x, y, board, player_char, opp_char):

	diagonal_char_count = 1
	empty_space_count = 0

	# Checking Left and Up
	i, j = x, y
	while(i != 0 and j != 0):

		current_char = board[i-1][j-1]

		if current_char == player_char:
			diagonal_char_count += 1
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
	while(i != BOARD_DIM and j != BOARD_DIM):

		current_char = board[i+1][j+1]

		if current_char == player_char:
			diagonal_char_count += 1
			i+=1
			j+=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break


	# Returning the appropriate case numbers

	if diagonal_char_count <= 1 or empty_space_count == 0:
		return 0

	elif diagonal_char_count == 2:
		return 3

	elif diagonal_char_count == 3:
		if empty_space_count == 1:
			return 2
		elif empty_space_count == 2:
			return 1


def check_diagonal_up(x, y, board, player_char, opp_char):

	diagonal_char_count = 1
	empty_space_count = 0

	# LEFT AND DOWN
	i, j = x, y

	while(j != BOARD_DIM and i != 0):

		current_char = board[i-1][j+1]

		if current_char == player_char:
			diagonal_char_count += 1
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

	while(j != 0 and i != BOARD_DIM):

		current_char = board[i+1][j-1]

		if current_char == player_char:
			diagonal_char_count += 1
			i+=1
			j-=1
			continue

		elif current_char == opp_char:
			break

		elif current_char == EMPTY_CHAR:
			empty_space_count += 1
			break
	# Returning the appropriate case numbers

	if diagonal_char_count <= 1 or empty_space_count == 0:
		return 0

	elif diagonal_char_count == 2:
		return 3

	elif diagonal_char_count == 3:
		if empty_space_count == 1:
			return 2
		elif empty_space_count == 2:
			return 1
