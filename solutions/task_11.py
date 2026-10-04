def guests_by_seat(seats):
    n = len(seats)
    result = [0] * n
    
    for guest_id in range(n):
        seat_num = seats[guest_id]
        
        result[seat_num - 1] = guest_id + 1
        
    return result

if __name__ == '__main__':
    user_input = input().strip()
    
    if user_input:
        user_seats = [int(x) for n in user_input.split()]
        ans = guests_by_seat(user_seats)
        print(*(ans))
