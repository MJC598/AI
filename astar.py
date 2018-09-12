import copy

def expand_node(puzzle_node):

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
        expanded_nodes.append(copy.deepcopy(puzzle_node))
        puzzle_node[i][j], puzzle_node[i+1][j] = puzzle_node[i+1][j], puzzle_node[i][j]

    # If the empty space is in the bottom 3 rows,
    # add a node that represents moving the empty space up
    if i > 0:
        puzzle_node[i][j], puzzle_node[i-1][j] = puzzle_node[i-1][j], puzzle_node[i][j]
        expanded_nodes.append(copy.deepcopy(puzzle_node))
        puzzle_node[i][j], puzzle_node[i-1][j] = puzzle_node[i-1][j], puzzle_node[i][j]

    # If the empty space is in the left three columns,
    # add a node that represents the empty space moving to the right
    if j < 3:
        puzzle_node[i][j], puzzle_node[i][j+1] = puzzle_node[i][j+1], puzzle_node[i][j]
        expanded_nodes.append(copy.deepcopy(puzzle_node))
        puzzle_node[i][j], puzzle_node[i][j+1] = puzzle_node[i][j+1], puzzle_node[i][j]

    # If the empty space is in the right three columns,
    # add a node that represents the empty space moving to the left
    if j > 0:
        puzzle_node[i][j], puzzle_node[i][j-1] = puzzle_node[i][j-1], puzzle_node[i][j]
        expanded_nodes.append(copy.deepcopy(puzzle_node))
        puzzle_node[i][j], puzzle_node[i][j-1] = puzzle_node[i][j-1], puzzle_node[i][j]

    return expanded_nodes

def get_manhattan(puzzle_node):

    manhattan_distance = 0

    for i in range(4):
        for j in range(4):

            if puzzle_node[i][j] == 0:
                continue
            manhattan_distance = manhattan_distance + abs(i - (puzzle_node[i][j]/4)) + abs(j -(puzzle_node[i][j] % 4))
    return manhattan_distance


if __name__ == '__main__':

    test_case_1 = [[1,2,7,3],[5,6,11,4],[9,10,15,8],[13,14,12,0]]
    test_case_2 = [[5,1,7,3],[9,2,11,4],[13,6,15,8],[0,10,14,12]]