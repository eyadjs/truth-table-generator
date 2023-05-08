from formats import transform, makeTable
from parentheses import valid_parentheses


def compute():

    x = input('Enter your logical statement: ')
    eq = transform(x) # ([ ['T', 'AND', 'T', ')'], ... , ... , ...],
                         # ['p', 'and', 'q', ')'],
                         # ['p','q'] ])

    # error handling
    if len(eq[2]) not in (2,3):
        return 'Please use 2 or 3 variables.'
    if valid_parentheses(eq[1]) == False:
        return 'Fix your parentheses.'
    

    return makeTable(x)

    
print(compute())
