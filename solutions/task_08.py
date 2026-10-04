from datetime import date

def century_message(name, age, current_year):
    year_of_100 = current_year + (100 - age)

    res = f"{name}, тебе исполнится 100 лет в {year_of_100} году"
    return res

if __name__ == '__main__':
    user_name = input()
    user_age = int(input())
    
    curr_year = day.today().year

    msg = century_message(user_name, user_age, curr_year)
    print(msg)
