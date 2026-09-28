def is_power_of_two(n):
    if n <= 0:
        return False
    return bin(n).count('1') == 1

if __name__ == '__main__':
    num = int(input("Введите целое число n:"))
    ans = is_power_of_two(num)
    print(f"Результат проверки: {ans}")
