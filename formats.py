def transform(x):
    
    table = []

    convert = {'NOT':['not','negate','negation','~'],
               'AND':['and','conjunction','^'],
               'OR':['or','disjunction','V'],
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
    final_split = x.split() # not used, purely so ['p', 'or', '(', 'q'] can be returned at the end

    
    for i in range(len(eq_list)):
        for k,v in convert.items():
            if eq_list[i] in v:
                eq_list[i] = k

    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    eq = ' '.join(eq_list)
    for i in eq_list:
        if i not in convert:
            if i not in alphabet:
                pass
                


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
        
    combos_2,combos_3 = [],[]

    for i in ['T','F']:
        for j in ['T','F']:
            combos_2.append(i + ' | ' + j)


    for i in ['T','F']:
        for j in ['T','F']:
            for k in ['T','F']:
                combos_3.append(i + ' | ' + j + ' | ' + k)



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

    return table, final_split