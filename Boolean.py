#!/usr/bin/python

# input cases
# !P and !Q
# (!P implication !Q) and Q implication P
# P equivalence Q and !R or Z

import re
import itertools

def get_variables(expression):
    return set(re.findall(r"\b(\w)\b", expression))

def construct_variable_truth_combinations(variables):
    n_variables = len(variables)
    return set(itertools.combinations([1, 0] * n_variables, n_variables))
    

print(construct_variable_truth_combinations(get_variables("P equivalence Q and !R or Z")))
print(get_variables("(!P implication !Q) and Q implication P"))
print(get_variables("!P and !Q or R"))
