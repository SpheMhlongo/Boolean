#!/usr/bin/python

# input cases
# !P and !Q
# (!P implication !Q) and Q implication P
# P equivalence Q and !R or Z

import re

def get_variables(expression):
    return re.findall(r"\b(\w)\b", expression)

print(get_variables("P equivalence Q and !R or Z"))
print(get_variables("(!P implication !Q) and Q implication P"))
print(get_variables("!P and !Q or R"))
