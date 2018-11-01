#this function takes a clause_list and returns a csp
from utils import argmin_random_tie, count, first
from csp import *

def first_unassigned_variable(assignment, csp):
    return first([var for var in csp.variables if var not in assignment])

def unordered_domain_values(var, assignment, csp):
    #return all values from var that aren't ruled out
    return csp.choices(var)

def no_inference(csp, var, value, assignment, removals):
    return True

def disjunction_constraint(clause):

    for var in clause:
        if var == True:
            return True

    return False

def clause_list_to_csp(clause_list):
    '''csp constructor is below

            def __init__(self, variables, domains, neighbors, constraints):

       we need to take the clause list which is a list of lists formatted as ['x1', 'x2', 'x3' ... size]
       where size is given in clause_list[0][2] and the number of distinct clause lists in clause_list is given at clause_list[0][3]
       1. variables is x1, x2, x3,... size:
       can we just have a loop that creates a set of variables from [1...size]?
       2. domains are T/F for each variable. E for not evaluated yet
       3. neighbors 
       4. constraints

    '''
    num_vars = int(clause_list[0][2])
    num_clauses = int(clause_list[0][3])
    variables = []
    domains = []

    for x in range(num_vars):
        #appends each of the variables 1-num_vars
        variables.append(x)
        #adds 'E' to the domains list for each variable
        domains.append('E')


#this search is the exact same as in-class provided code
#https://github.com/aimacode/aima-python 
def backtracking_search(csp, selected_unassigned_variable = first_unassigned_variable, \
                        order_domain_values = unordered_domain_values, inference = no_inference):
    
    def backtrack(assignment):
        #if length of assignment list == length of variables list return assignment list
        if len(assignment) == len(csp.variables):
            return assignment
        #this runs mrv
        var = selected_unassigned_variable(assignment, csp)
        #for each value in var that hasn't been removed
        for value in order_domain_values(var, assignment, csp):
            #if there are no conflicts
            if 0 == csp.nconflicts(var, value, assignment):
                #assign a value to the csp
                csp.assign(var, value, assignment)
                #add to the list of removals the new values
                removals = csp.suppose(var, value)
                #if forward checking is true
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result is not None:
                        return result
                csp.restore(removals)
        csp.unassign(var, assignment)
        return None

    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result

def mrv(assignment, csp):
    return argmin_random_tie(
        [v for v in csp.variables if v not in assignment],
        key=lambda var: num_legal_values(csp, var, assignment))

def num_legal_values(csp, var, assignment):
    #remaining values that can still work for variables
    if csp.curr_domains:
        return len(csp.curr_domains[var])
    else:
        return count(csp.nconflicts(var, val, assignment) == 0 for val in csp.domains[var])

def forward_checking(csp, var, value, assignment, removals):
    #removes values from domain
    csp.support_pruning()
    #for each of the neighbors
    for B in csp.neighbors[var]:
        #if the neighbor is not in the assignment
        if B not in assignment:
            #for each value in avaliable domains
            for b in csp.curr_domains[B][:]:
                #if the constraint doesn't work
                if not csp.constraints(var, value, B, b):
                    #remove the value from the list
                    csp.prune(B, b, removals)
            #if no value is avaliable, the tree fails
            if not csp.curr_domains[B]:
                return False
    return True
