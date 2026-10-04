def max_of_three(a, b, c):
    res = max(a, b, c)
    return res

if __name__ == '__main__':
    inputs = []
    for _ in range(3):
        user_input = input()
        num = float(user_input) if '.' in user_input else int(user_input)
        inputs.append(num)
    ans = max_of_three(inputs[0], inputs[1], inputs[2])
    print(ans)
