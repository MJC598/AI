from time import clock
from copy import deepcopy
from random import randint
from heuristic import *

#this takes the board and evaluates the heuristic to return to the minimax tree
def minimax_exec(board, player):
    opponent_symbol = 'E'
    player_symbol = 'E'
    if player == 'p1':
        player_symbol = 'X'
        opponent_symbol = 'O'
    else:
        player_symbol = 'O'
        opponent_symbol = 'X'
    #initialize return vars
    winner = None
    #previous moves (list of coordinate pairs)
    x_list = []
    o_list = []
    #possible moves (list of coordinate pairs)
    action_list = []
    #fill the lists with coordinate pairs of possible moves and all previous moves
    for x in range(6):
        for y in range(6):
            if board[x][y] == 'E':
                action_list.append(tuple((x,y)))
            elif board[x][y] == 'X':
                x_list.append(tuple((x,y)))
                x_check_value = heuristic(x, y, board, 'X', 'O')
                if(x_check_value == 1000000000):
                    winner = 'p1'
                    return tuple((winner, None))
            else:
                o_list.append(tuple((x,y)))
                y_check_value = heuristic(x, y, board, 'O', 'X')
                if(y_check_value == 1000000000):
                    winner = 'p2'
                    return tuple((winner, None))
    #verify there are still possible moves on the board
    if not action_list:
        winner = 'tie'
        return tuple((winner, None))

    #sort each of the lists by the first number of the coordinate pair, it can make it easier to compare
    x_list.sort(key=lambda tup: tup[0])
    o_list.sort(key=lambda tup: tup[0])
    action_list.sort(key=lambda tup: tup[0])

    h_value_list = []

    temp_board = board.copy()
    print_board(board)
    # print_board(temp_board)
    #returns the max of the min value and the correct move
    choice = min_value(action_list, temp_board, player_symbol, opponent_symbol, 0)
    move = choice[1]
    print_board(board)

    #move is a coordinate pair tuple
    return tuple((winner,move))

# ************************************
#
#END OF HEURISTIC FUNCTION
#
# ************************************

def min_value(action_list, board, player_char, opp_char, increment):
    value_list = []
    if player_char == 'X':
        # print('p1 min')
        if increment == 2:
            value_list = []
            for action in action_list:
                # print('hey, im in the min_value but p1')
                value_list.append(tuple((heuristic(action[0], action[1], update_board(board, player, action), player_char, opp_char), action)))
            return min(value_list)
        else:
            value_list = []
            for action in action_list:
                value_list.append(max_value(action_list, update_board(board, player, action), player_char, opp_char, increment+1))
            return min(value_list)
    else:
        # print('p2 min')
        if increment == 4:
            value_list = []
            for action in action_list:
                value_list.append(tuple((heuristic(action[0], action[1], update_board(board, player, action), player_char, opp_char), action)))
            return min(value_list)
        else:
            value_list = []
            for action in action_list:
                value_list.append(max_value(action_list, update_board(board, player, action), player_char, opp_char, increment+1))
            return min(value_list)



def max_value(action_list, board, player_char, opp_char, increment):
    value_list = []
    if player_char == 'X':
        # print('p1 max')
        if increment == 2:
            value_list = []
            for action in action_list:
                # print('hey, im in the max_value, but p1')
                value_list.append(tuple((heuristic(action[0], action[1], update_board(board, player, action), player_char, opp_char), action)))
            return max(value_list)
        else:
            value_list = []
            for action in action_list:
                value_list.append(min_value(action_list, update_board(board, player, action), player_char, opp_char, increment+1))
            return max(value_list)
    else:
        # print('p2 max')
        if increment == 4:
            value_list = []
            for action in action_list:
                # print('hey, im in the max value, but p2')
                value_list.append(tuple((heuristic(action[0], action[1], update_board(board, player, action), player_char, opp_char), action)))
            return max(value_list)
        else:
            value_list = []
            for action in action_list:
                value_list.append(min_value(action_list, update_board(board, player, action), player_char, opp_char, increment+1))
            return max(value_list)

#call the heuristic to get the correct move and then execute it. Looks ahead 2 moves (1 for opp, 1 for me)
#if the game is over, it returns the winner and the board (in a tuple)
#otherwise, board and blank
def minimax_tree(board, player):
    winner = None
    winner, choice = minimax_exec(board, player)
    if choice is None:
        return tuple((winner, board))
    new_board = update_board(board, player, choice)
    print_board(new_board)
    return tuple((winner, new_board))

#updates board according to player
def update_board(board, player, choice):
    symbol = 'X'
    if player == 'p2':
        symbol = 'O'
    #Change board spot out with the appropriate symbol
    board[choice[0]][choice[1]] = symbol
    return board

#pretty self-explanatory, prints the board
def print_board(board):
    for x in range(6):
        for y in range(6):
            print(board[x][y], end='')
            print(' ', end='')
        print('\n', end='')
    print('------------------')

#start of main
if __name__ == "__main__":
    #winner_list will hold the results of all the games
    winner_list = []
    x_win = 0
    o_win = 0
    ties = 0
    player = 'p2'
    winner = None
    '''
        E - Empty
        X - p1
        O - p2
    '''
    #empty board
    new_board = [['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E']]
    #initial update puts the first move for p1 in the middle of the board
    offset1 = randint(0,1)
    offset2 = randint(0,1)
    board = update_board(new_board, player, (2+offset1,2+offset2))
    #run this 100 times to get new winners each time?
    #return p1, p2, or tie breaks the loop
    while winner is None:
        #check to see who played last, alternates between p1 and p2
        if(player == 'p1'):
            player = 'p2'
            winner, board = minimax_tree(board, player)
            if winner != None:
                if winner == 'p2':
                    winner_list.append("p2")
                    o_win += 1
                else:
                    ties += 1
                break
        else:
            player = 'p1'
            winner, board = minimax_tree(board, player)
            if winner != None:
                if winner == 'p1':
                    winner_list.append("p1")
                    x_win += 1
                else:
                    ties += 1
    winner_list.append(winner)
    #print victory board
    print_board(board)
