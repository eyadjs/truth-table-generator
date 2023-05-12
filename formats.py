from calculators import regular_calculator
from tabulate import tabulate
from parentheses import parentheses_calculator

def transform(x):
    
    table = []

    convert = {'NOT':['not','negate','negation','~','*'],
               'AND':['and','conjunction','^','&'],
               'OR':['or','disjunction','V','|'],
               'IMPLIES':['implies','implication','->','=>'],
               'IMPLIES2':['biconditional','biimplies','double implies','<=>','<->']}
    

    x = list(x)

    for i in range(len(x)):
        if x[i] == '(':
            x[i] = ' ( '
        if x[i] == ')':
            x[i] =  ' ) '
    
    
    x = ''.join(x)
    eq_list = x.split() # used
    

    
    for i in range(len(eq_list)):
        for k,v in convert.items():
            if eq_list[i] in v:
                eq_list[i] = k

    final_split = eq_list # not used, purely so ['p', 'or', '(', 'q'] can be returned at the end
    

    alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    eq = ' '.join(eq_list)
    for i in eq_list:
        if i not in convert:
            if i not in alphabet:
                pass # ???????????????????????????????
                


    n = 0
    variables = []
    for i in range(len(eq_list)):
        if eq_list[i] in alphabet:
            
            variables.append(eq_list[i])
            alphabet.remove(eq_list[i])
 
    n=len(variables)
    

    if n in (0,1) or n > 3:
        return 'Please use 2 or 3 distinct variables!'
    
    if n == 2:
        
        a2,b2,c2,d2 = eq,eq,eq,eq
        
        for i in ['T','F']:
            for j in ['T','F']:
                for l in [a2,b2,c2,d2]:
                    l = l.replace(variables[0],i)
                    l = l.replace(variables[1],j)
                    table.append(l.split())
                    break

    if n == 3:
        a3,b3,c3,d3,e3,f3,g3,h3 = eq,eq,eq,eq,eq,eq,eq,eq
        for i in ['T','F']:
            for j in ['T','F']:
                for k in ['T','F']:
                    for l in [a3,b3,c3,d3,e3,f3,g3,h3]:
                        l = l.replace(variables[0],i)
                        l = l.replace(variables[1],j)
                        l = l.replace(variables[2],k)
                        table.append(l.split())
                        break

    return (table, final_split, variables)


def makeTable(x):

    eq = transform(x)
    

    # making the expression look nice eg. p and q ----> p ∧ q

    final_touch_dict = {'AND':'∧','OR':'∨','NOT':'¬','IMPLIES':'⇒','IMPLIES2':'⇔'}
    
    final_touch = eq[1] # ['p','AND','q']

    
    
    for i in range(len(final_touch)):
        if final_touch[i] in final_touch_dict:
            final_touch[i] = final_touch_dict[final_touch[i]]
    eq_pretty = ' '.join(final_touch) # eg. p ∧ q



    table = [] # [['T'], ['F'], ['F'], ['F']]

    if '(' in eq[0][1]:
        for i in range(len(eq[0])):
            eq[0][i] = parentheses_calculator(eq[0][i])


    for i in range(len(eq[0])):
        table.append(regular_calculator(eq[0][i]))





    variables = eq[2] # ['p','q']
    variables_table = ''

    # formatting the variables so I can have p | q in the table 

    for i in range(len(variables)):
        variables_table += variables[i]
        variables_table += ' | '

    variables_table = variables_table[:-3] # 'p | q'



            
    combos_2,combos_3 = [],[] # preset T/F combos eg. TT | TF | ...

    for i in ['T','F']:
        for j in ['T','F']:
            combos_2.append(i + ' | ' + j)

    for i in ['T','F']:
        for j in ['T','F']:
            for k in ['T','F']:
                combos_3.append(i + ' | ' + j + ' | ' + k)
    
    
    headers = [variables_table, eq_pretty]
    
    if len(variables) == 2:
        table_content_2 = [[combos_2[i], ''.join(table[i])] for i in range(len(table))]
        return tabulate(table_content_2, headers)
    if len(variables) == 3:
        table_content_3 = [[combos_3[i], ''.join(table[i])] for i in range(len(table))]
        return tabulate(table_content_3, headers)








help_table_headers = ["Operation","Accepted Inputs"]
help_table_operations = ["Negation","Conjunction","Disjunction","Implication","Bi-implication" ]
help_table_inputs = ['not, negate, negation, ~, *',
                    'and, conjunction, ^, &,'
                    ,'or, disjunction, V, |',
                    'implies, implication, ->, =>',
                    'biconditional, biimplies, double implies, <=>, <->']
help_table_contents = [[help_table_operations[i], ''.join(help_table_inputs[i])] for i in range(len(help_table_inputs))]
help_table = '\n\nEnter a propositional statement using up to 3 variables in the alphabet.\nFor example: p and (q or r)' + '\n\n\nAccepted inputs for operations are as follows:\n\n'+ tabulate(help_table_contents, help_table_headers)