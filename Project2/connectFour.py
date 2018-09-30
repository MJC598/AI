

if __name__ == "__main__":
    #winner_list will hold the results of all the games
    winner_list = []
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
    #initial run of the p1_minimax_tree with a clean board
    winner, board = p1_minimax_tree(new_board)
    #run this 100 times to get new winners each time?
    while winner is None:
        #since we already ran p1 we start the loop with p2
        winner, board = p2_minimax_tree(board)
        #if p2 is the winner, we have to break the loop so we don't continue running a p1 tree
        if winner not None:
            winner_list.append("p2")
            break
        #if p2 cannot find a winner, p1 runs
        winner, board = p1_minimax_tree(board)
        if winner not None:
            #we don't need to break here because this is the end of the loop, it is done automatically
            winner_list.append("p1")
    
    winner_list.append(winner)




#this takes the board and evaluates the heuristic to return to the minimax tree
def heuristic(board, player):
    #initialize as neutral 0
    value = 0
    '''
        h(n) = 5*[# of 2-side open 3-in-a-row for me]
               -10*[# of 2-side open 3-in-a-row for opp]
               +3*[# of 1-side open 3-in-a-row for me]
               -6*[# of 1-side open 3-in-a-row for opp]
               +[# of open 2-in-a-row for me]
               -[# of open 2-in-a-row for opp]

               use 
    '''
    return value

#call the heuristic to get the correct move and then execute it. Looks ahead 2 moves (1 for opp, 1 for me)
#if the game is over, it returns the winner and the board (in a tuple)
#otherwise, board and blank
def p1_minimax_tree(board):
    player = 'p1'
    winner = None
    new_board = board
    choice = heuristic(board, player)
    new_board = update_board(board, player)

    return tuple((winner, new_board))


#same as p1_minimax_tree except this one looks ahead 4 moves (2 for opp, 2 for me)
#if the game is over, it returns the winner and the board (in a tuple)
#otherwise, board and blank
def p2_minimax_tree(board):
    player = 'p2'
    winner = None
    new_board = board
    choice = heuristic(board, player)
    new_board = update_board(board, player)

    return tuple((winner, new_board))

#updates board according to player
def update_board(board, player):
    new_board = board

    return new_board

#pretty self-explanatory, prints the board
def print_board(board):
    for x in range(6):
        for y in range(6):
            print(board[x][y], end='')
            print(' ', end='')
        print('\n', end='')
    print('------------------')
