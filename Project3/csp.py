#Much of this code is designed based on the code given to us in class and found on:
#https://github.com/aimacode/aima-python 
#specifically the csp.py and search.py files

from utils import is_in, count

#This abstract class is pulled directly from the cited source on search.py
class Problem(object):

    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise NotImplementedError

#This CSP class is pulled directly from the cited source on csp.py
class CSP(Problem):
    def __init__(self, variables, domains, neighbors, constraints):
        variables = variables or list(domains.keys())

        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.initial = ()
        self.curr_domains = None
        self.nassigns = 0

    #assign the val passed to the var in the assignment list
    def assign(self, var, val, assignment):
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
        #return the number conflicts var=val has with other variables
        def conflict(var2):
            return (var2 in assignment and not self.constraints(var, val, var2, assignment[var2]))
        print(self.neighbors)
        return count(conflict(v) for v in self.neighbors[var]) 

    #display the CSP and the assignment list
    def display(self, assignment):
        print('CSP: ', self, 'with assignment: ', assignment)

    #pass the current state and return 
    def actions(self, state):
        if len(state) == len(self.variables):
            return []
        else:
            assignment = dict(state)
            var = first([v for v in self.variables if v not in assignment])
            return [(var, val) for val in self.domains[var] if self.nconflicts(var, val, assignment) == 0]

    def result(self, state, action):
        #perform an action and return the new state
        (var, val) = action
        return state + ((var, val),)

    def goal_test(self, state):
        #assign all variables with all constraints satisfied
        assignment = dict(state)
        return (len(assignment) == len(self.variables) 
            and all(self.nconflicts(variables, assignment[variables], assignment) == 0 
                for variables in self.variables))

    def support_pruning(self):
        #only prune values from domains if able
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def suppose(self, var, value):
        #create inference list from assuming var=value
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        self.curr_domains[var] = [value]
        return removals

    def prune(self, var, value, removals):
        #makes sure var != value
        self.curr_domains[var].remove(value)
        if removals is not None:
            removals.append((var, value))

    def choices(self, var):
        #return all values for var that aren't ruled out
        return (self.curr_domains or self.domains)[var]

    def infer_assignment(self):
        #return the partial assignment implied by the current inferences
        self.support_pruning()
        return {v: self.curr_domains[v][0] for v in self.variables if 1 == len(self.curr_domains[v])}

    def restore(self, removals):
        #put everything back
        for B, b in removals:
            self.curr_domains[B].append(b)

    def conflicted_vars(self, current):
        #returns list of conflicted variables
        return [var for var in self.variables if self.nconflicts(var, current[var], current) > 0]
