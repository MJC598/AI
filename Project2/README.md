# AI
Implementation of Artificial Intelligence Programs for Mizzou CMP_SC 4750

## Members
* Matthew Carroll
* David Huangal

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

A little caveat, since the first move is randomized to one of the four middle nodes, it can change the rest of the nodes. Also, the algorithm takes a while to work on the p2 choices and when p2 goes first it works significantly faster. 

```
E E E E E E 
E E E E E E 
E E E X E E 
E E E E E E 
E E E E E E 
E E E E E E 
------------------
Time:  7.155565096309017e-05
E E E E E E 
E O E E E E 
E E E X E E 
E E E E E E 
E E E E E E 
E E E E E E 
------------------
Time:  89.64820397538307
Total Nodes:  48904880
E E E E E E 
E O E E E E 
E E E X E E 
E E E E X E 
E E E E E E 
E E E E E E 
------------------
Time:  0.23334120001049996
Total Nodes:  33540
E E E E E E 
E O O E E E 
E E E X E E 
E E E E X E 
E E E E E E 
E E E E E E 
------------------
Time:  90.49346554684294
Total Nodes:  60935035
E E E E E E 
E O O E E E 
E E E X X E 
E E E E X E 
E E E E E E 
E E E E E E 
------------------
Time:  0.23082564110086423
Total Nodes:  50496
```


#### Turned Around (P2 plays first)

```
E E E E E E 
E E E E E E 
E E E O E E 
E E E E E E 
E E E E E E 
E E E E E E 
------------------
Time:  8.266677688903585e-05
E E E E E E 
E X E E E E 
E E E O E E 
E E E E E E 
E E E E E E 
E E E E E E 
------------------
Time:  0.24157454432161465
Total Nodes:  24716
E E E E E E 
E X E E E E 
E E E O E E 
E E E O E E 
E E E E E E 
E E E E E E 
------------------
Time:  93.14534597157241
Total Nodes:  56533764
E E E E E E 
E X X E E E 
E E E O E E 
E E E O E E 
E E E E E E 
E E E E E E 
------------------
Time:  0.2249718555180209
Total Nodes:  42021
E E E E E E 
E X X E E E 
E E E O O E 
E E E O E E 
E E E E E E 
E E E E E E 
------------------
Time:  87.31239863875373
Total Nodes:  66671180

```