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
from clause_list_to_csp import *
from plotly import __version__
from plotly.offline import plot
import plotly.graph_objs as go

def file_to_line_list(filename):
    """
    Creates a list of lines from the file, where each line is
    a list of tokens split by whitespace.
    e.g. the line "p cnf 3 5" would be added to the list as:
    ['p', 'cnf', '3', '5']

    returns list of clauses
    first clause is always formatted ['p', 'cnf', '# of variables', '# of clauses']
    following are all lists of clauses that terminate with a '0' (which is pulled off below)
    """
    clause_list = []
    with open(filename, "r") as file:
        for line in file:
            # rstrip() removes the '\n' newline character
            clause_list.append(line.rstrip().split())

    num_vars = clause_list[0][2]
    num_clauses = clause_list[0][3]
    #removing 0s at the end of each list except the first one
    for x in clause_list:
        if x[0] not 'p':
            del x[-1]

    return clause_list


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

def mrv(assignment, csp):
    return argmin_random_tie(
        [v for v in csp.variables if v not in assignment],
        key=lambda var: num_legal_values(csp, var, assignment))

def num_legal_values(csp, var, assignment):
    if csp.curr_domains:
        return len(csp.curr_domains[var])
    else:
        return count(csp.nconflicts(var, val, assignment) == 0 for val in csp.domains[var])

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

#this is all the stuff to graph the data
def plot_it(results1, results2, results3, results4):
    e1 = go.Scatter(x=1, y=results1, name='Example 1 Results')
    e2 = go.Scatter(x=2, y=results2, name='Example 2 Results')
    e3 = go.Scatter(x=3, y=results3, name='Example 3 Results')
    e4 = go.Scatter(x=4, y=results4, name='Example 4 Results')

    data = [e1, e2, e3, e4]
    layout = go.Layout(title='CSP Results', xaxis=dict(title='Variable ID'), yaxis=dict(title='True/False Value'))
    fig = go.Figure(data = data, layout = layout)
    plot_url = plot(fig, filename='results.html')


if __name__ == "__main__":
    beginning_time = clock()
    #plot each of the results
    plot_it(backtracking_search(clause_list_to_csp(file_to_line_list("example1.txt")), select_unassigned_variable=mrv, inference=forward_checking), 
        backtracking_search(clause_list_to_csp(file_to_line_list("example2.txt")), select_unassigned_variable=mrv, inference=forward_checking), 
        backtracking_search(clause_list_to_csp(file_to_line_list("example3.txt")), select_unassigned_variable=mrv, inference=forward_checking), 
        backtracking_search(clause_list_to_csp(file_to_line_list("example4.txt")), select_unassigned_variable=mrv, inference=forward_checking))
    end_time = clock()
    print("Time: ", end_time - beginning_time)


