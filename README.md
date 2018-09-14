# AI
Implementation of Artificial Intelligence Programs for Mizzou CMP_SC 4750

## Members
* Matt Carroll
* David Huangal
---
## A*
### Implementation:

The manhattan is calculated like this:
```python
manhattan_distance = 0

	for i in range(4):
		for j in range(4):
			number = puzzle_node[i][j]
			if number != i * 4 + (j+i) and number != 0:
				correct_i = (number - 1) // 4
				correct_j = (number - 1) % 4
				manhattan_distance += abs(i - correct_i) + abs(j - correct_j)
```

Expand node is a function that returns a list of tuples of the format: (list of possible states, letter representing movement). Here is a quick example of adding an downward movement:
```python
# If the empty space is in the top three rows,
	# add a node that represents moving the empty space down
	if i < 3:
		puzzle_node[i][j], puzzle_node[i+1][j] = puzzle_node[i+1][j], puzzle_node[i][j]
		expanded_nodes.append((deepcopy(puzzle_node), "D"))
		puzzle_node[i][j], puzzle_node[i+1][j] = puzzle_node[i+1][j], puzzle_node[i][j]

```

The astar function uses a priority queue for which each item has the format: (manhattan distance + level + 1 i.e. the total cost, level, current state, current solution).

While the fringe is not empty, I get the next item out of the priority queue and check if it is equivalent to the solution. If so, I return the correct solution sequence e.g. "DRDDL" etc.

If it is not the correct solution, I'll expand the current state, and if the node hasn't been seen before, I'll evaluate it's manhattan distance, add it to the visited list and put an item into the priority queue like so:

```python
for node, instruction in expanded_nodes:
			node_tuple = create_tuple(node)

			if node_tuple not in visited_nodes:
				manhattan_distance = get_manhattan_distance(node)
				visited_nodes.add(node_tuple)

				fringe.put((manhattan_distance + level + 1 , level+1, node, current_answer+instruction))

```
And continue until the solution is found or 1000000 nodes are expanded.
