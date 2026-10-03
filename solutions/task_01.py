def meters_to_centimeters(meters):
    a = meters * 100
    return a

if __name__ == '__main__':
    user_input =input("Distance in centimeters: ")

    m = float(user_input) if '.' in user_input else int(user_input)
    cm = meters_to_centimeters(m)

    print(f"Distance in centimeters: {cm}")