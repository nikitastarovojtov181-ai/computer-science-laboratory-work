def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == '__main__':
    user_input_x = input()
    x = float(user_input_x) if '.' in user_input_x else int(user_input_x)

    user_input_y = input()
    y = float(user_input_y) if '.' in user_input_y else int(user_input_y)

    x, y = swap(x, y)
    print(x, y)
