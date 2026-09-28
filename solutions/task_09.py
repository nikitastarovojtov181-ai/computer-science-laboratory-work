def max_of_three(a, b, c):
    res = max(a, b, c)
    return res

if __name__ == '__main__':
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))

    ans = max_of_three(num1, num2, num3)
    print(f"Наибольшее число: {ans}")
