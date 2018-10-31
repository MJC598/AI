"""
Implementation of backtracking search using MRV and degree heuristic
and forward checking to solve the Boolean Satisfiability Problem
or SAT.

Note
--------------------

Although we can solve it this way, the problem is NP-Complete and
therefore, we may not be solving it in the most efficient way.
"""
from utils import argmin_random_tie, count, first
from time import clock
from copy import deepcopy
from csp import *
from plotly import __version__
from plotly.offline import plot
import plotly.graph_objs as go

def file_to_line_list(filename):
    """
    Creates a list of lines from the file, where each line is
    a list of tokens split by whitespace.
    e.g. the line "p cnf 3 5" would be added to the list as:
    ['p', 'cnf', '3', '5']

    returns list of constraints
    first constraint is always formatted ['p', 'cnf', '# of variables', '# of clauses']
    following are all lists of clauses that terminate with a '0' (which is pulled off below)
    """
    constraints = []
    with open(filename, "r") as file:
        for line in file:
            # rstrip() removes the '\n' newline character
            constraints.append(line.rstrip().split())

    num_vars = constraints[0][2]
    num_clauses = constraints[0][3]
    #removing 0s at the end of each list except the first one
    for x in constraints:
        if x[0] not 'p':
            del x[-1]

    return constraints

#this search is the exact same as in-class provided code
#https://github.com/aimacode/aima-python 
def backtracking_search(csp, 
    selected_unassigned_variable = first_unassigned_variable, 
    order_domain_values = unordered_domain_values, 
    inference = no_inference):
    
    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment
        var = selected_unassigned_variable(assignment, csp)
        for value in order_domain_values(var, assignment, csp):
            if 0 == csp.nconflicts(var, value, assignment):
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value)
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

if __name__ == "__main__":
    ex1 = "example1.txt"
    ex2 = "example2.txt"
    ex3 = "example3.txt"
    ex4 = "example4.txt"
    constraints1 = file_to_line_list(ex1)
    constraints2 = file_to_line_list(ex2)
    constraints3 = file_to_line_list(ex3)
    constraints4 = file_to_line_list(ex4)

    #this is all the stuff to graph the data
    e1 = go.Scatter(x=1, y=results1, name='Example 1 Results')
    e2 = go.Scatter(x=2, y=results2, name='Example 2 Results')
    e3 = go.Scatter(x=3, y=results3, name='Example 3 Results')
    e4 = go.Scatter(x=4, y=results4, name='Example 4 Results')

    data = [e1, e2, e3, e4]
    layout = go.Layout(title='CSP Results', xaxis=dict(title='Variable ID'), yaxis=dict(title='True/False Value'))
    fig = go.Figure(data = data, layout = layout)
    plot_url = plot(fig, filename='results.html')
