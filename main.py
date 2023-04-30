from formats import transform
from parantheses import valid_parantheses
from calculators import regular_calculator

def compute():

    x = input('Enter your logical statement: ')
    eq = transform(x) #eg. ([['T', 'AND', 'T', ')'], ... , ... , ...], ['p', 'and', 'q', ')'])

    if valid_parantheses(eq[1]) == False:
        return 'Fix your parantheses!'
    
    return regular_calculator(eq[0])

    
print(compute())
