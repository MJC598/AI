

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
    #empty board
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
    #print victory board
    print_board(board)

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

    '''
    maybe traverse action_list and see if they meet any of the requirements to add to a,b,c,d,e,f? 
    This would require we check every square around each action_list node like:
        1 2 3
        4 X 5
        6 7 8
    meaning a max branching factor of 8. However, if the action_list is a corner, then:
        1 2
        3 X
    which would have a branching factor of 3...
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
    #traverse board and change it out with the appropriate symbol
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
