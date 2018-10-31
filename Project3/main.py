"""
Implementation of backtracking search using MRV and degree heuristic
and forward checking to solve the Boolean Satisfiability Problem
or SAT.

Note
--------------------

Although we can solve it this way, the problem is NP-Complete and
therefore, we may not be solving it in the most efficient way.
"""
from time import clock
from copy import deepcopy
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

    The first clause is always formatted ['p', 'cnf', '# of variables', '# of clauses']
    following are all lists of clauses that terminate with a '0' (which is pulled off below)

    returns list of clauses
    """
    clause_list = []
    with open(filename, "r") as file:
        for line in file:
            # rstrip() removes the '\n' newline character
            clause_list.append(line.rstrip().split())

    # Final formatting of the list
    for x in range(len(clause_list) + 1):
        # Remove 0's that denote end of a line
        del clause_list[x][-1]

        # Convert each variable in the clause from string to int
        for v in range(len(clause[x])):
            clause[x][v] = int(clause[x][v])

    return clause_list

#this is all the stuff to graph the data
def plot_it(results1, results2, results3, results4):
    e1 = go.Scatter(x=[1], y=results1, name='Example 1 Results')
    e2 = go.Scatter(x=[2], y=results2, name='Example 2 Results')
    e3 = go.Scatter(x=[3], y=results3, name='Example 3 Results')
    e4 = go.Scatter(x=[4], y=results4, name='Example 4 Results')

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


