from formats import transform, makeTable
from parantheses import valid_parantheses


def compute():

    x = input('Enter your logical statement: ')
    eq = transform(x) # ([ ['T', 'AND', 'T', ')'], ... , ... , ...],
                         # ['p', 'and', 'q', ')'],
                         # ['p','q'] ])

    isParantheses = False 
    # checking if parantheses handling is needed
    for i in eq[1]:
        if i in (')','('):
            isParantheses = True


    # error handling
    if len(eq[2]) not in (2,3):
        return 'Please use 2 or 3 variables.'
    if valid_parantheses(eq[1]) == False:
        return 'Fix your parantheses.'
    
    
    if isParantheses == True:
        return 'Parantheses handling coming soon.'
    else:
        return makeTable(x)

    
print(compute())
