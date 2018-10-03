from time import clock
from copy import deepcopy
from random import random

#this takes the board and evaluates the heuristic to return to the minimax tree
def heuristic(board, player):
    #initialize return vars
    winner = None
    #previous moves (list of coordinate pairs)
    x_list = []
    o_list = []
    #possible moves (list of coordinate pairs)
    action_list = []
    #variables for number of evaulatable matches
    a = b = c = d = e = f = 0
    #fill the lists with coordinate pairs of possible moves and all previous moves
    for x in range(6):
        for y in range(6):
            if board[x][y] == 'E':
                action_list.append(tuple((x,y)))
            elif board[x][y] == 'X':
                x_list.append(tuple((x,y)))
                x_check_value = check_around(board, x, y, 'X')
                if(x_check_value == 4):
                    winner = 'p1'
                    return tuple((winner, None))
            else:
                o_list.append(tuple((x,y)))
                y_check_value = check_around(board, x, y, 'O')
                if(y_check_value == 4):
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
    '''
    what if we set it up with a sort of ring situation, where it starts in the center(2,2/3,2/2,3/3,3) and traverse out
        on X's and O's from there? Or what if we have a 2nd array where we keep putting coordinate pairs connected to 1 we 
        pop out of the x_list and count the number in the array? Something like:
        tail = ()
        active = x_list.pop()
        around = ()
        if around active
            around.add
        tail.add(active)
        active = around.pop()

        or what if we count it in the initial traversal of the board? 
            Like go up, up-right, right, right-down, down, down-left, left, left-up whenever we find an X and if there is 
            one already continue going in the same direction. I think this might be the best way to go

    layout of initial board with 1st move is:

          0 1 2 3 4 5 (*these indicies are for personal use, not actually on board)
        0 E E E E E E
        1 E E E E E E 
        2 E E X E E E
        3 E E E E E E
        4 E E E E E E
        5 E E E E E E 

    maybe traverse action_list and see if they meet any of the requirements to add to a,b,c,d,e,f? 
    It would speed up every move, but would be incredibly slow at first
    This would require we check every square around each action_list node like:
        1 2 3
        4 X 5
        6 7 8
    meaning a max branching factor of 8. However, if the action_list is a corner, then:
        1 2
        3 X
    which would have a max branching factor of 3...
    We might be able to keep track of this from the previous board iteration too making it have to do much less work?


    This is the heuristic function:

        h(n) = 5*[# of 2-side open 3-in-a-row for me (a)]
               -10*[# of 2-side open 3-in-a-row for opp (b)]
               +3*[# of 1-side open 3-in-a-row for me (c)]
               -6*[# of 1-side open 3-in-a-row for opp (d)]
               +[# of open 2-in-a-row for me (e)]
               -[# of open 2-in-a-row for opp (f)]

               use 
    '''

    #move is a coordinate pair tuple
    return tuple((winner,move))

# ************************************
#
#END OF HEURISTIC FUNCTION
#
# ************************************

#check each of the squares around the active block
def check_around(board, x, y, value):
    if(x != 0 or board[x-1][y] == value):
        #left
        return 1+check_left(board, x-1, y, value)
    elif(x != 0 or y != 0 or board[x-1][y-1] == value):
        #left-up
        return 1+check_left_up(board, x-1, y-1, value)
    elif(y != 0 or board[x][y-1] == value):
        #up
        return 1+check_up(board, x, y-1, value)
    elif(x != 6 or y != 0 or board[x+1][y-1] == value):
        #up-right
        return 1+check_up_right(board, x+1, y-1, value)
    elif(x != 6 or board[x+1][y] == value):
        #right
        return 1+check_right(board, x+1, y, value)
    elif(x != 6 or y != 6 or board[x+1][y+1] == value):
        #right-down
        return 1+check_right_down(board, x+1, y+1, value)
    elif(y != 6 or board[x][y+1] == value):
        #down
        return 1+check_down(board, x, y+1, value)
    elif(x != 0 or y != 6 or board[x-1][y+1] == value):
        #left-down
        return 1+check_down_left(board, x-1, y+1, value)
    else:
        #returns the number of adjacent blocks
        return 1

#sorry for the disgusting helper functions but I'm kinda at the point of brute forcing it...
def check_left(board, x, y, value):
    if(x != 0 or board[x-1][y] == value):
        return 1 + check_left(board, x-1, y, value)
    else:
        return 0

def check_left_up(board, x, y, value):
    if(x != 0 or y != 0 or board[x-1][y-1] == value):
        return 1 + check_left_up(board, x-1, y-1, value)
    else:
        return 0

def check_up(board, x, y, value):
    if(y != 0 or board[x][y-1] == value):
        return 1 + check_up(board, x, y-1, value)
    else:
        return 0

def check_up_right(board, x, y, value):
    if(x != 6 or y != 0 or board[x+1][y-1] == value):
        return 1 + check_up_right(board, x+1, y-1, value)
    else:
        return 0

def check_right(board, x, y, value):
    if(x != 6 or board[x+1][y] == value):
        return 1 + check_right(board, x+1, y, value)
    else:
        return 0

def check_right_down(board, x, y, value):
    if(x != 6 or y != 6 or board[x+1][y+1] == value):
        return 1 + check_right_down(board, x+1, y+1, value)
    else:
        return 0

def check_down(board, x, y, value):
    if(y != 6 or board[x][y+1] == value):
        return 1 + check_down(board, x, y+1, value)
    else:
        return 0

def check_down_left(board, x, y, value):
    if(x != 0 or y != 6 or board[x-1][y+1] == value):
        return 1 + check_down_left(board, x-1, y+1, value)
    else:
        return 0

#call the heuristic to get the correct move and then execute it. Looks ahead 2 moves (1 for opp, 1 for me)
#if the game is over, it returns the winner and the board (in a tuple)
#otherwise, board and blank
def minimax_tree(board, player):
    winner = None
    winner, choice = heurisitc(board, player)
    if choice is None:
        return tuple((winner, board))
    new_board = update_board(board, player, choice)
    return tuple((winner, new_board))

#updates board according to player
def update_board(board, player, choice):
    symbol = 'X'
    if player == 'p2':
        symbol = 'O'
    new_board = board
    #Change board spot out with the appropriate symbol
    new_board[choice[0]][choice[1]] = symbol
    return new_board

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
    player = 'p1'
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
    offset1 = random(0,1)
    offset2 = random(0,1)
    board = update_board(new_board, player, (2+offset1,2+offset2))
    #run this 100 times to get new winners each time?
    #return p1, p2, or tie breaks the loop
    while winner is None:
        #check to see who played last, alternates between p1 and p2
        if(player == 'p1'):
            player = 'p2'
            winner, board = minimax_tree(board, player)
            if winner not None:
                if winner == 'p2':
                    winner_list.append("p2")
                    o_win += 1
                else:
                    ties += 1
                break
        else:
            player = 'p1'
            winner, board = minimax_tree(board, player)
            if winner not None:
                if winner == 'p1':
                    winner_list.append("p1")
                    x_win += 1
                else:
                    ties += 1
    winner_list.append(winner)
    #print victory board
    print_board(board)
