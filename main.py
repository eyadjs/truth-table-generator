from formats import *
from parentheses import valid_parentheses

<<<<<<< HEAD
def compute(x):
=======
def compute():
>>>>>>> c80e629a0be31a159d5c9dccf540d9292408812c

    help_menu = help_table

    # while True:

    #     print("\n\nEnter 'h' for help menu\nEnter 'p' to generate a truth table")

<<<<<<< HEAD
    #     key = input()
    #     if key.lower() == 'h':
    #         pass
    #         print(help_menu)
        
    #     if key.lower() == 'p':
    eq = transform(x) # ([ ['T', 'AND', 'T', ')'], ... , ... , ...], [0]
                        # ['p', 'and', 'q', ')'], [1]
                        # ['p','q'] ]) [2]

    # error handling
    if len(eq[2]) not in (2,3):
        return 'Please use 2 or 3 lowercase variables.'
    if valid_parentheses(eq[1]) == False:
        return 'Fix your parentheses.'

    return makeTable(x) # make it take in x!!!!!!!!!!
    
# print(compute())
=======
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
>>>>>>> c80e629a0be31a159d5c9dccf540d9292408812c
