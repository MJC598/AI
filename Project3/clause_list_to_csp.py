#this function takes a clause_list and returns a csp
from csp import *
def clause_list_to_csp(clause_list):
    '''csp constructor is below

            def __init__(self, variables, domains, neighbors, constraints):

       we need to take the clause list which is a list of lists formatted as ['x1', 'x2', 'x3' ... size]
       where size is given in clause_list[0][2] and the number of distinct clause lists is given at clause_list[0][3]
       
    '''