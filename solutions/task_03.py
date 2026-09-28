def is_divisor(a, b):
    if a == 0:
        return False
    if b % a == 0:
        return True
    else:
        return False

if __name__ == '__main__':

    num_a = int(input("Введите число a: "))
    num_b = int(input("Введите число b: "))

    ans = is_divisor(num_a, num_b)
    print(f"Результат проверки: {ans}")
