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
    return list(set(itertools.combinations([1, 0] * n_variables, n_variables)))

def NOT(operand):
	return not operand

def OR(operand1, operand2):
	return operand1 or operand2

def XOR(operand1, operand2):
	return (operand1 or operand2) and not (operand1 and operand2) 

def AND(operand1, operand2):
	return operand1 and operand2

def IMPLICATION(operand1, operand2):
	return not (operand1 and not operand2)

def EQUIVALENCE(operand1, operand2):
	return operand1 and operand2 or not operand1 and not operand2

def assign(variables, values):
	return list(zip(list(variables), values))

def assign_values(variables):
	assigned_variables = []
	for values in construct_variable_truth_combinations(variables):
		assigned_variables.append(assign(variables, values))
	return [ assign(variables, values) for values in construct_variable_truth_combinations(variables)]

# order of importance
# NOT
# XOR
# AND
# OR
# IMPLICATION
# EQUIVALENCE

def parse(args):
	pass


variables = get_variables("P and Q implication R")
truths = construct_variable_truth_combinations(variables)

print(assign(variables, truths[0]))

print(construct_variable_truth_combinations(get_variables("P equivalence Q and !R or Z")))
print(get_variables("(!P implication !Q) and Q implication P"))
print(get_variables("!P and !Q or R"))

print(truths)
print(assign_values(variables))

print(IMPLICATION(1, 1))
print(IMPLICATION(1, 0))
print(IMPLICATION(0, 1))
print(IMPLICATION(0, 0))