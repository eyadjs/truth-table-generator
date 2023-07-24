def negation(i):
        
        while '¬' in i:
            while '-' in i:
                i.remove('-')
            for j in range(len(i)):
                if i[j] == '¬':
                    if i[j+1] == 'F':
                        i[j+1] = 'T'
                    else:
                        i[j+1] = 'F'
                    i[j] = '-'
                    break
        while '-' in i:
            i.remove('-')
        return i

def conjunction(i):
        
        while '∧' in i:
            while '-' in i:
                i.remove('-')
            for j in range(len(i)):
                if i[j] == '∧':
                    if i[j-1] =='T' and i[j+1] == 'T':
                        i[j] = 'T'
                    else:
                        i[j] = 'F'
                    i[j-1] ='-'
                    i[j+1] = '-'
                    break
        while '-' in i:
            i.remove('-')
        return i

def disjunction(i):
        
        while '∨' in i:
            while '-' in i:
                i.remove('-')
            for j in range(len(i)):
                if i[j] == '∨':
                    if i[j-1] =='F' and i[j+1] == 'F':
                        i[j] = 'F'
                    else:
                        i[j] = 'T'
                    i[j-1] ='-'
                    i[j+1] = '-'
        while '-' in i:
            i.remove('-')
        return i

def implication(i):
        
        while '⇒' in i:
            while '-' in i:
                i.remove('-')
            for j in range(len(i)):
                if i[j] == '⇒':
                    if i[j-1] == 'T' and i[j+1] == 'F':
                        i[j] = 'F'
                    else:
                        i[j] = 'T'
                    i[j-1] ='-'
                    i[j+1] = '-'
                    break

        while '-' in i:
            i.remove('-')
        
        return i

def biimplication(i):
        
        while '⇔' in i:
            while '-' in i:
                i.remove('-')
            for j in range(len(i)):
                if i[j] == '⇔':
                    if i[j-1] == i[j+1]:
                        i[j] = 'T'
                    else:
                        i[j] = 'F'
                    i[j-1] ='-'
                    i[j+1] = '-'
                    break
        while '-' in i:
            i.remove('-')
        return i

def regular_calculator(table):

    # in the default order of precedence 
    table = negation(table)
    table = conjunction(table)
    table = disjunction(table)
    table = implication(table)
    table = biimplication(table)

    return table
