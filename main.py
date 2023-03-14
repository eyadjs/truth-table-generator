from tabulate import tabulate

def format():


    eq = input('Enter a propositional logic formula: ')    
    table = []

    convert = {'NOT':['not','negate','negation','^'],
               'AND':['and','conjunction'],
               'OR':['or','disjunction'],
               'IMPLIES':['implies','implication'],
               'IMPLIES2':['biconditional','biimplies','double implies','<=>','<->']}
    
    
    eq_list = eq.split()

    for i in range(len(eq_list)):
        for k,v in convert.items():
            if eq_list[i] in v:
                eq_list[i] = k

    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    eq = ' '.join(eq_list)
    for i in eq_list:
        if i not in convert:
            if i not in alphabet:
                return 'Invalid symbols!'


    n = 0
    variables = []
    for i in range(len(eq_list)):
        if eq_list[i] in alphabet:
            
            variables.append(eq_list[i])
            alphabet.remove(eq_list[i])
 
    n=len(variables)
    

    if n > 3:
        return 'Please use a maximum of 3 variables!'
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


    for i in table: # NEGATION
        while 'NOT' in i:
            while '-' in i:
                i.remove('-')
            for j in range(len(i)):
                if i[j] == 'NOT':
                    if i[j+1] == 'F':
                        i[j+1] = 'T'
                    else:
                        i[j+1] = 'F'
                    i[j] = '-'
                    break
    for i in table:
        while '-' in i:
            i.remove('-')


    for i in table: # AND
        while 'AND' in i:
            while '-' in i:
                i.remove('-')
            for j in range(len(i)):
                if i[j] == 'AND':
                    if i[j-1] =='T' and i[j+1] == 'T':
                        i[j] = 'T'
                    else:
                        i[j] = 'F'
                    i[j-1] ='-'
                    i[j+1] = '-'
                    break
    for i in table:
        while '-' in i:
            i.remove('-')

    for i in table: # OR
        while 'OR' in i:
            while '-' in i:
                i.remove('-')
            for j in range(len(i)):
                if i[j] == 'OR':
                    if i[j-1] =='F' and i[j+1] == 'F':
                        i[j] = 'F'
                    else:
                        i[j] = 'T'
                    i[j-1] ='-'
                    i[j+1] = '-'
                    break
                
    
    for i in table:
        while '-' in i:
            i.remove('-')
    
    for i in table: # IMPLES
        while 'IMPLIES' in i:
            while '-' in i:
                i.remove('-')
            for j in range(len(i)):
                if i[j] == 'IMPLIES':
                    if i[j-1] == 'T' and i[j+1] == 'F':
                        i[j] = 'F'
                    else:
                        i[j] = 'T'
                    i[j-1] ='-'
                    i[j+1] = '-'
                    break
    for i in table:
        while '-' in i:
            i.remove('-')
    
    for i in table: # IMPLES
        while 'IMPLIES2' in i:
            while '-' in i:
                i.remove('-')
            for j in range(len(i)):
                if i[j] == 'IMPLIES2':
                    if i[j-1] == i[j+1]:
                        i[j] = 'T'
                    else:
                        i[j] = 'F'
                    i[j-1] ='-'
                    i[j+1] = '-'
                    break

    for i in table:
        while '-' in i:
            i.remove('-')



    dict = {}
    if n == 2:
        for i in range(len(table)):
            dict[combos_2[i]] = table[i]
    if n == 3:
        for i in range(len(table)):
            dict[combos_3[i]] = table[i]
    
    data = [[k,''.join(v)] for k,v in dict.items()]

    final_touch_dict = {'AND':'∧','OR':'∨','NOT':'¬','IMPLIES':'⇒','IMPLIES2':'⇔'}

    final_touch = eq.split()
    for i in range(len(final_touch)):
        if final_touch[i] in final_touch_dict:
            final_touch[i] = final_touch_dict[final_touch[i]]
    eq = ' '.join(final_touch)

    headers = ['p | q | r', eq]

    print('The proposition')
    if n == 2:
        return tabulate(data, headers=[variables[0] + '|' + variables[1], eq])
    if n == 3:
        return tabulate(data, headers=[variables[0] + '|' + variables[1] + '|' + variables[2], eq])

print(format())


    




