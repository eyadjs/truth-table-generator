def regular_calculator(table):
    
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
    
    for i in table: # BI-IMPLIES
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

    return table