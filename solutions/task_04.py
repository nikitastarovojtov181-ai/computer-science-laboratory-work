def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == '__main__':
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))

    print(f"До обмена: x = {x}, y = {y}")

    x, y = swap(x, y)
    print(f"После обмена: x = {x}, y = {y}")
