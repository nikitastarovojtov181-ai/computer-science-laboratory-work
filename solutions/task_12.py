def shortest_distance(kilometers, meters):
    km_in_m = kilometers * 1000

    if km_in_m < meters:
        return km_in_m
    else:
        return meters

if __name__ == '__main__':
    km = float(input("Enter kilometers: "))
    m = float(input("Enter meters: "))

    ans = shortest_distance(km, m)
    print(f"Shortest distance in meters: {ans}")
