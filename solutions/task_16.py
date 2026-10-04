def month_calendar(start_weekday, days):
    calendar_days = []

    for _ in range(start_weekday):
        calendar_days.append(" ")

    for day in range(1, days + 1):
        calendar_days.append(f"{day:2}")

    weeks = []

    for i in range(0, len(calendar_days), 7):
        week_chunk = calendar_days[i:i + 7]
        
        while len(week_chunk) < 7:
            week_chunk.append(" ")
            
        week_str = " ".join(week_chunk)
        weeks.append(week_str)
            
    return "\n".join(weeks)

if __name__ == '__main__':
    s_day = int(input())
    t_days = int(input())

    result = month_calendar(s_day, t_days)
    print(result)

    result = month_calendar(w_day, total_days)
    print("\nВаш календарь: ")
    print(result)
        
