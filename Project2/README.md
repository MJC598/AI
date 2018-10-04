# AI
Implementation of Artificial Intelligence Programs for Mizzou CMP_SC 4750

## Members
* Matthew Carroll
* David Huangal
---
## Hardware / Software
These algorithms were written for Python 3. We ran them on a MacBook Pro on macOS High Sierra with a 2.9 GHz Intel Core i5 Processor and 16 GB of Memory.

### Connect 4 AI with Minimax Tree Implementation
---
#### Heuristic Implementation

The heuristic function matches the one specified for us. We traverse the graph looking for groups of 'X's and check to see if they have openings on the ends. If it does it adds it to the appropriate list and gets the total number by taking the length of the list. It then uses these totals in the heuristic function to get a value.
```python
    p_tto = len(player_three_two_open)
    p_too = len(player_three_one_open)
    p_to = len(player_two_open)

    o_tto = len(opponent_three_two_open)
    o_too = len(opponent_three_one_open)
    o_to = len(opponent_two_open)

    heuristic = (5 * p_tto) - (10 * o_tto) + (3 * p_too) - (6 * o_too) + p_to - o_to
```

#### Minimax Tree Implementation

The minimax tree alternates back and forth between min and max value by the iterator (the last value carried in the function call). Below is the first call to start the search of the tree. The values returned are a tuple of the heuristic value and the appropriate move, and the total node generated count.  
```python
choice, total_nodes = max_value(action_list, temp_board, player_symbol, player_win, opp_win, opponent_symbol, 0)
```

After this call, it alternates back and forth till it reaches the terminal level when it calls the heuristic function, as seen below.

```python
value, nodes = heuristic(action[0], action[1], update_board(temp_board, player, action), player_char, opp_char, player_win, opp_win)
```

after this call, it unwinds the recursion and gives the correct move.

#### First Five Boards

A little caveat, since the first move is randomized to one of the four middle nodes, it can change the rest of the nodes.

```


```


#### Turned Around (P2 plays first)

```


```