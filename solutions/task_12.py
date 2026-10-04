def shortest_distance(kilometers, meters):
    km_in_m = kilometers * 1000

    if km_in_m < meters:
        return km_in_m
    else:
        return meters

if __name__ == '__main__':
    user_input_km = input()
    km = float(user_input_km) if '.' in user_input_km else int(user_input_km)

    user_input_m = input()
    m = float(user_input_m) if '.' in user_input_m else int(user_input_m)

    ans = shortest_distance(km, m)
    print(ans)
