def multiplication_table(n):
    table = []
    for i in range(1, 11):
        res = n * i
        row = f"{n} x {i} = {res}"
        table.append(row)
    return table

if __name__ == '__main__':
    num = int(input())
    ans = multiplication_table(num)

    for string in ans:
        print(string)
