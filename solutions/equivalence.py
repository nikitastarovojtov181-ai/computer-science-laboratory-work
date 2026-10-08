def are_equivalent(f, g, n):
    table = truth_table(n)
    
    for row in table:
        if f(*row) != g(*row):
            return False
            
    return True

def truth_table(n):
    table = [()]
    for _ in range(n):
        new_table = []
        for row in table:
            new_table.append(row + (0,))
            new_table.append(row + (1,))
        table = new_table
    return table

def f1(x, y):
    return not (x and y)

def g1(x, y):
    return (not x) or (not y)

def g2(x, y):
    return (not x) and y

if __name__ == '__main__':

    print("f1 и g1 эквивалентны:", are_equivalent(f1, g1, 2))
    print("f1 и g2 эквивалентны:", are_equivalent(f1, g2, 2))
