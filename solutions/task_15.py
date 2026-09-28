def days_in_month(month, year):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31

if __name__ == '__main__':
    m = int(input("Введите номер месяца (1-12): "))
    y = int(input("Введите четырехзначный год: "))

    ans = days_in_month(m, y)
    print(f"Колличество дней: {ans}")
