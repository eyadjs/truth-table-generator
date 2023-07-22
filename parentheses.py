from calculators import *

def valid_parentheses(x):

    eq_list = x # eg. ['(,'p','and','q',')']

    if ')(' in eq_list:
        return False
    
    only_p = []
    for i in eq_list:
        if i in['(',')']:
            only_p.append(i) # eg. ['(',')']
    stack = []
    lookup = {')':'('}

    for p in only_p:
        if p == ')(':
            return False
        if p in lookup.values():
            stack.append(p)
        elif stack and lookup[p] == stack[-1]:
            stack.pop()
        else:
            return False
        
    return stack == []

def parentheses_calculator(test):
    
    if '(' not in test:
        return regular_calculator(test)

    op_i = 0  # deepest opening index
    cl_i = 0  # corresponding closing index
    for i in range(len(test)):
        if test[i] == '(':
            op_i = i
        if test[i] == ')':
            cl_i = i
            break

    sub_expression_result = regular_calculator(test[op_i + 1:cl_i])
    test = test[:op_i] + sub_expression_result + test[cl_i + 1:]

    if cl_i - op_i == 2:
        test = test[:op_i] + '-' + test[cl_i + 1:]

    while '-' in test:
        test = test.replace('-', '')

    return parentheses_calculator(test)
