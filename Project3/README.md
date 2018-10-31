# AI
Implementation of Artificial Intelligence Programs for Mizzou CMP_SC 4750

## Members
* Matthew Carroll
* David Huangal

## Hardware / Software
These algorithms were written for Python 3. We ran them on a MacBook Pro on macOS High Sierra with a 2.9 GHz Intel Core i5 Processor and 16 GB of Memory.

### Boolean Satisfiability Problem using MRV and degree heurisitics and Forward Checking
---
### Heuristic Implementation

This problem uses Minimum Remaining Value (MRV) and Degrees for its primary heuristic and tiebreaker implementation. MRV is implemented here:
```python
def mrv(assignment, csp):
    return argmin_random_tie(
        [v for v in csp.variables if v not in assignment],
        key=lambda var: num_legal_values(csp, var, assignment))
```

and degree heuristic is implemented here:
```python


```

### Forward Checking

Forward checking checks all possible situations by moving forward and assuming assignments to each node and making sure there is still a valid path forward. If the path is discovered to have a node without a satisfiable domain, the path is thrown out as invalid. It is implemented here:
```python
def forward_checking(csp, var, value, assignment, removals):
    csp.support_pruning()
    for B in csp.neighbors[var]:
        if B not in assignment:
            for b in csp.curr_domains[B][:]:
                if not csp.constraints(var, value, B, b):
                    csp.prune(B, b, removals)
            if not csp.curr_domains[B]:
                return False
    return True
```

### Instance 1
```


```

### Instance 2
```


```

### Instance 3
```


```

### Instance 4
```


```

### Plotted Graph
```


```