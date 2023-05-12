from formats import *
from parentheses import valid_parentheses


def compute():

    help_menu = help_table

    while True:

        print("\n\nEnter 'h' for help menu\nEnter 'p' to generate a truth table")

        key = input()
        if key.lower() == 'h':
            pass
            print(help_menu)
        
        if key.lower() == 'p':
            x = input('Enter your logical statement: ')
            eq = transform(x) # ([ ['T', 'AND', 'T', ')'], ... , ... , ...], [0]
                                # ['p', 'and', 'q', ')'], [1]
                                # ['p','q'] ]) [2]

            # error handling
            if len(eq[2]) not in (2,3):
                return 'Please use 2 or 3 lowercase variables.'
            if valid_parentheses(eq[1]) == False:
                return 'Fix your parentheses.'


            return makeTable(x)


    
print(compute())
