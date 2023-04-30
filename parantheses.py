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