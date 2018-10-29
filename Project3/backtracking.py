from time import clock
from copy import deepcopy

def file_to_line_list(filename):
    """
    Creates a list of lines from the file, where each line is
    a list of tokens split by whitespace.
    e.g. the line "p cnf 3 5" would be added to the list as:
    ['p', 'cnf', '3', '5']

    returns list of lines
    """
    lines = []

    with open(filename) as file:
        for line in file:
            # rstrip() removes the '\n' newline character
            lines.append(line.rstrip().split())

    return lines


if __name__ == "__main__":
    pass
