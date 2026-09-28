def sum_interval(a, b):
    start = min(a, b)
    end = max(a, b)

    count = end - start + 1

    res = (start + end) * count // 2
    return res

if __name__ == '__main__':
    num1 = int(input("Введите число a:"))
    num2 = int(input("Введите число b:"))

    ans = sum_interval(num1, num2)
    print(f"Сумма в интервале: {ans}")
