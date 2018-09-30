

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
            else:
                o_list.append(tuple((x,y)))
    #verify there are still possible moves on the board
    if not action_list:
        winner = 'tie'
        return tuple((winner, None))

    #sort each of the lists by the first number of the coordinate pair, it can make it easier to compare
    x_list.sort(key=lambda tup: tup[0])
    o_list.sort(key=lambda tup: tup[0])
    action_list.sort(key=lambda tup: tup[0])
    '''
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
    board = update_board(new_board, player, (2,2))
    #run this 100 times to get new winners each time?
    #return p1, p2, or tie breaks the loop
    while winner is None:
        #check to see who played last, alternates between p1 and p2
        if(player == 'p1')
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