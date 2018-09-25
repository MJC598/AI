# AI
Implementation of Artificial Intelligence Programs for Mizzou CMP_SC 4750

## Members
* Matthew Carroll
* David Huangal
---
## Hardware / Software
These algorithms were written for Python 3. We ran them on a MacBook Pro on macOS High Sierra with a 2.9 GHz Intel Core i5 Processor and 16 GB of Memory.

## IDS
### Implementation:
The IDS works by continuously supplying a depth of a tree from 0 to the solution is found and restarting the built tree from each depth increase.
The depth increase happens here:
```python
limit = 0
		result = Result(-1, 0, problem)
		#constantly loop until solution is found
		while(result.count < 1000000):
			result = self.depthLimitedSearch(problem, goal, limit)
			limit += 1
			#this is the check for node otherwise continue looping
			if(result.value != 0):
				return result
```

Then, a standard BFS is implemented which implements a LIFO queue, like here:
```python
#traverse list of nodes to expand recursively
for successor in nodeList:
				result = self.recursiveDLS(successor, result.count, problem, goal, limit)
				if(result.value == 0):
					cutoff = True
				elif(result.value != -1):
					return result
```

Finally, if the tree generates over 1 million nodes the IDS exits with the understanding that the tree is too big
```python
while(result.count < 1000000):
	#if the while loop fails result is set to -2
result.value = -2
return result

#where result is returned in order to indicate 1000000 nodes
elif(result.value is -2):
		print(result.count)
		print(ctime.microseconds, end='')
		print(" microseconds")
		print("Reached 1000000 nodes program was terminated!")
```

### First Five Nodes:
#### Test Case 1
```
01 02 07 03
05 06 11 04
09 10 15 00
13 14 12 08
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 00 12
--------------------
01 02 07 03
05 06 11 04
09 10 15 00
13 14 12 08
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 00 12
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 12 00
--------------------

```
#### Test Case 2
```
05 01 07 03
09 02 11 04
00 06 15 08
13 10 14 12
--------------------
05 01 07 03
09 02 11 04
13 06 15 08
10 00 14 12
--------------------
05 01 07 03
09 02 11 04
00 06 15 08
13 10 14 12
--------------------
05 01 07 03
09 02 11 04
13 06 15 08
10 00 14 12
--------------------
05 01 07 03
09 02 11 04
13 06 15 08
00 10 14 12
--------------------

```
### Solution Found:
#### Test Case 1
```
01 02 03 04
05 06 07 08
09 10 11 12
13 14 15 00
--------------------
01 02 03 04
05 06 07 08
09 10 11 00
13 14 15 12
--------------------
01 02 03 04
05 06 07 00
09 10 11 08
13 14 15 12
--------------------
01 02 03 00
05 06 07 04
09 10 11 08
13 14 15 12
--------------------
01 02 00 03
05 06 07 04
09 10 11 08
13 14 15 12
--------------------
01 02 07 03
05 06 00 04
09 10 11 08
13 14 15 12
--------------------
01 02 07 03
05 06 11 04
09 10 00 08
13 14 15 12
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 00 12
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 12 00
--------------------
nodes created: 5294
time taken to execute: 353186 microseconds

```
#### Test Case 2
```
520246 microseconds
Reached 1000000 nodes program was terminated!

```

## DFGS
### Implementation:
A DFGS operates as a Depth First Search on a graph. The key difference is that the graph search recognizes which nodes have already been visited. That is being done here:
```python
#closing nodes to recongize where the graph has already been traversed
if node not in closed:
	closed.append(node)
	nodeList = self.expand(node.state, node, problem)
```

Otherwise, the same FIFO queue implmentation is still happening:
```python
#fringe is discovered graph
fringe = [node]
while(len(fringe) <= 1000000):
	if(fringe == []):
		result.value = -1
		return result
	node = fringe.pop(0)

#putting nodes on fringe
for x in nodeList:
	fringe.append(x)
```

And the DFGS also exits after 1 million nodes, which takes substantially longer because it doesn't repeat nodes like an IDS does. That is accounted for here:
```python
while(len(fringe) <= 1000000):
	#functioning code goes here
	#this is if the result.count value hits 1 million
	if(result.count >= 1000000):
		result.value = -2
		return result

elif(result.value is -2):
	print(result.count)
	print(ctime.microseconds, end='')
	print(" microseconds")
	print("Reached 1000000 nodes program was terminated!")
```

### First Five Nodes:
#### Test Case 1
```
01 02 07 03
05 06 11 04
09 10 15 00
13 14 12 08
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 00 12
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 12 00
--------------------
01 02 07 03
05 06 11 00
09 10 15 04
13 14 12 08
--------------------
01 02 07 03
05 06 11 04
09 10 00 15
13 14 12 08
--------------------

```
#### Test Case 2
```
05 01 07 03
09 02 11 04
00 06 15 08
13 10 14 12
--------------------
05 01 07 03
09 02 11 04
13 06 15 08
10 00 14 12
--------------------
05 01 07 03
09 02 11 04
13 06 15 08
00 10 14 12
--------------------
05 01 07 03
00 02 11 04
09 06 15 08
13 10 14 12
--------------------
05 01 07 03
09 02 11 04
06 00 15 08
13 10 14 12
--------------------

```
### Solution Found:
#### Test Case 1
```
01 02 03 04
05 06 07 08
09 10 11 12
13 14 15 00
--------------------
01 02 03 04
05 06 07 08
09 10 11 00
13 14 15 12
--------------------
01 02 03 04
05 06 07 00
09 10 11 08
13 14 15 12
--------------------
01 02 03 00
05 06 07 04
09 10 11 08
13 14 15 12
--------------------
01 02 00 03
05 06 07 04
09 10 11 08
13 14 15 12
--------------------
01 02 07 03
05 06 00 04
09 10 11 08
13 14 15 12
--------------------
01 02 07 03
05 06 11 04
09 10 00 08
13 14 15 12
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 00 12
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 12 00
--------------------
nodes created: 20914
time taken to execute: 923522 microseconds

```
#### Test Case 2
```
881551 microseconds
Reached 1000000 nodes program was terminated!

```

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

### First 5 Nodes:
#### Test Case 1
```
Expanding Node Number: 0
01 02 07 03
05 06 11 04
09 10 15 08
13 14 12 00
--------------------
Expanding Node Number: 1
01 02 07 03
05 06 11 04
09 10 15 08
13 14 00 12
--------------------
Expanding Node Number: 2
01 02 07 03
05 06 11 04
09 10 00 08
13 14 15 12
--------------------
Expanding Node Number: 3
01 02 07 03
05 06 00 04
09 10 11 08
13 14 15 12
--------------------
Expanding Node Number: 4
01 02 00 03
05 06 07 04
09 10 11 08
13 14 15 12
--------------------

```
#### Test Case 2
```
Expanding Node Number: 0
05 01 07 03
09 02 11 04
13 06 15 08
00 10 14 12
--------------------
Expanding Node Number: 1
05 01 07 03
09 02 11 04
00 06 15 08
13 10 14 12
--------------------
Expanding Node Number: 2
05 01 07 03
00 02 11 04
09 06 15 08
13 10 14 12
--------------------
Expanding Node Number: 3
00 01 07 03
05 02 11 04
09 06 15 08
13 10 14 12
--------------------
Expanding Node Number: 4
01 00 07 03
05 02 11 04
09 06 15 08
13 10 14 12
--------------------

```
### Solution Found:
#### Test Case 1
```
Expanded Count:  9
01 02 07 03
05 06 11 04
09 10 15 08
13 14 12 00
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 00 12
--------------------
01 02 07 03
05 06 11 04
09 10 00 08
13 14 15 12
--------------------
01 02 07 03
05 06 00 04
09 10 11 08
13 14 15 12
--------------------
01 02 00 03
05 06 07 04
09 10 11 08
13 14 15 12
--------------------
01 02 03 00
05 06 07 04
09 10 11 08
13 14 15 12
--------------------
01 02 03 04
05 06 07 00
09 10 11 08
13 14 15 12
--------------------
01 02 03 04
05 06 07 08
09 10 11 00
13 14 15 12
--------------------
01 02 03 04
05 06 07 08
09 10 11 12
13 14 15 00
--------------------
Solution found in  8 Steps!
Solution Sequence:  LUUURDDD
Time: 0.0022699999999999942
```
#### Test Case 2
```
Expanded Count:  35
05 01 07 03
09 02 11 04
13 06 15 08
00 10 14 12
--------------------
05 01 07 03
09 02 11 04
00 06 15 08
13 10 14 12
--------------------
05 01 07 03
00 02 11 04
09 06 15 08
13 10 14 12
--------------------
00 01 07 03
05 02 11 04
09 06 15 08
13 10 14 12
--------------------
01 00 07 03
05 02 11 04
09 06 15 08
13 10 14 12
--------------------
01 02 07 03
05 00 11 04
09 06 15 08
13 10 14 12
--------------------
01 02 07 03
05 06 11 04
09 00 15 08
13 10 14 12
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 00 14 12
--------------------
01 02 07 03
05 06 11 04
09 10 15 08
13 14 00 12
--------------------
01 02 07 03
05 06 11 04
09 10 00 08
13 14 15 12
--------------------
01 02 07 03
05 06 00 04
09 10 11 08
13 14 15 12
--------------------
01 02 00 03
05 06 07 04
09 10 11 08
13 14 15 12
--------------------
01 02 03 00
05 06 07 04
09 10 11 08
13 14 15 12
--------------------
01 02 03 04
05 06 07 00
09 10 11 08
13 14 15 12
--------------------
01 02 03 04
05 06 07 08
09 10 11 00
13 14 15 12
--------------------
01 02 03 04
05 06 07 08
09 10 11 12
13 14 15 00
--------------------
Solution found in  15 Steps!
Solution Sequence:  UUURDDDRUUURDDD
Time: 0.007444000000000006

```
