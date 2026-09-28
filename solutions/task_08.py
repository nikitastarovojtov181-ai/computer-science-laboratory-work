def century_message(name, age, current_year):
    year_of_100 = current_year + (100 - age)

    res = f"{name} will turn 100 years old in the year {year_of_100}"
    return res

if __name__ == '__main__':
    user_name = input("Enter name: ")
    user_age = int(input("Enter age: "))
    curr_year = int(input("Enter curren year: "))

    msg = century_message(user_name, user_age, curr_year)
    print(msg)
