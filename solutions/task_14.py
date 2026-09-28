def circle_diameter(radius):
    d = radius * 2
    return d

def sum_range(start, end):
    total = 0

    for i in range(start, end + 1):
        total = total + 1
    return total

if __name__ == '__main__':
    print("--- Проверка функции cirle_diameter ---")
    r = float(input("Введите радиус: "))
    print(f"Диаметр: {circle_diameter(r)}")

    print("\n--- Проверка функции sum_range ---")
    s = int(input("Введите начало диапазона (start): "))
    e = int(input("Введите конец диапазона (end): "))
    print(f"Сумма ряда: {sum_range(s, e)}")
