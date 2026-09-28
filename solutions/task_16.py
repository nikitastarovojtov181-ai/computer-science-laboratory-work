def month_calendar(start_weekday, days):
    calendar_days = []

    for _ in range(start_weekday):
        calendar_days.append(" ")

    for day in range(1, days + 1):
        calendar_days.append(f"{day:>2}")

    weeks = []

    for i in range(0, len(calendar_days), 7):
        week_chunk = calendar_days[i : i + 7]
        week_str = " ".join(week_chunk)
        week_str = week_str.rstrip()
        weeks.append(week_str)
    return "\n".join(weeks)

if __name__ == '__main__':
    w_day = int(input("Введите день недели для 1-го числа (0-6): "))
    total_days = int(input("Введите колличество дней в месяце: "))

    result = month_calendar(w_day, total_days)
    print("\nВаш календарь: ")
    print(result)
        
