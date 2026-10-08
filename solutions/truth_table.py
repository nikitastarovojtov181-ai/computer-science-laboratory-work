def truth_table(n):
    table = [()]

    for _ in range(n):
        new_table = []
        for row in table:
            new_table.append(row + (0,))
            new_table.append(row + (1,))
        table = new_table

    return table

if __name__ == '__main__':

    print(truth_table(1))
    print(truth_table(2))
    print(truth_table(3))
    print(truth_table(0))
