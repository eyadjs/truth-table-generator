from calculators import *
def valid_parantheses(x):

    eq_list = format(x)[1] # eg. ['(,'p','and','q',')']

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

    while '(' in test:

        op_i = 0 # deepest opening index
        cl_i = 0 # corresponding closing index
        for i in range(len(test)):
            if test[i] == '(':
                op_i = i
            if test[i] == ')':
                cl_i = i
                break


        test = test[:op_i+1] + regular_calculator(test[op_i+1:cl_i]) + test[cl_i:]

        if cl_i - op_i == 2:
            test[cl_i], test[op_i] = '-','-'
        while '-' in test:
            test.remove('-')
    
    return test