def meters_to_centimeters(meters):
    a = meters * 100
    return a

if __name__ == '__main__':
    m = float(input("Distance in meters: "))
    cm = meters_to_centimeters(m)
    print(f"Distance in centimeters: {cm}")
