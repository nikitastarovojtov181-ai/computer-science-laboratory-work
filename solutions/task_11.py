def guests_by_seat(seats):
    n = len(seats)
    result = [0] * n
    
    for guest_id in range(n):
        seat_num = seats[guest_id]
        
        result[seat_num - 1] = guest_id + 1
        
    return result

if __name__ == '__main__':
    user_input = input("Введите номера мест через пробел: ")
    test_seats = [int(x) for x in user_input.split()]

    if test_seats:
        ans = guests_by_seat(test_seats)
        print(f"Номера гостей по местам: {ans}")
