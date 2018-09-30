

if __name__ == "__main__":
    #winner_list will hold the results of all the games
    winner_list = []
    x_win = 0
    o_win = 0
    ties = 0
    player = 'p1'
    '''
        E - Empty
        X - p1
        O - p2
    '''
    new_board = [['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E'], 
                 ['E','E','E','E','E','E']]
    #initial run of the minimax_tree with a clean board and start with p1
    winner, board = minimax_tree(new_board, player)
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

#this takes the board and evaluates the heuristic to return to the minimax tree
def heuristic(board, player):
    #initialize return vars
    winner = None
    #previous moves
    x_list = []
    o_list = []
    #possible moves
    action_list = []

    #fill the lists with coordinate pairs of possible moves and all previous moves
    for x in range(6):
        for y in range(6):
            if board[x][y] == 'E':
                action_list.append(tuple(x,y))
            elif board[x][y] == 'X':
                x_list.append(tuple(x,y))
            else:
                o_list.append(tuple(x,y))
    #verify there are still possible moves on the board
    if not action_list:
        winner = 'tie'
        return tuple(winner, None)

    '''
        h(n) = 5*[# of 2-side open 3-in-a-row for me]
               -10*[# of 2-side open 3-in-a-row for opp]
               +3*[# of 1-side open 3-in-a-row for me]
               -6*[# of 1-side open 3-in-a-row for opp]
               +[# of open 2-in-a-row for me]
               -[# of open 2-in-a-row for opp]

               use 
    '''

    #move is a coordinate pair tuple
    return tuple(winner,move)

#call the heuristic to get the correct move and then execute it. Looks ahead 2 moves (1 for opp, 1 for me)
#if the game is over, it returns the winner and the board (in a tuple)
#otherwise, board and blank
def minimax_tree(board, player):
    winner = None
    choice = heurisitc(board, player)
    new_board = update_board(board, player, choice)
    return tuple((winner, new_board))

#updates board according to player
def update_board(board, player, choice):
    symbol = 'E'
    if player == 'p1':
        symbol = 'X'
    else:
        symbol = 'O'
    new_board = board
    for x in range(6):
        for y in range(6):
            if x == choice[0] and y == choice[1]:
                new_board[x][y] = symbol
    return new_board

#pretty self-explanatory, prints the board
def print_board(board):
    for x in range(6):
        for y in range(6):
            print(board[x][y], end='')
            print(' ', end='')
        print('\n', end='')
    print('------------------')
