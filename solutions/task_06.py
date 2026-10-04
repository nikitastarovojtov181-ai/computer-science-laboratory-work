def echo_number(number):
    res = f"Thats the number you entered {number}"
    return res

if __name__ == '__main__':
    user_input = input()
    num = float(user_input) if '.' in user_input else int(user_input)
    
    ans = echo_number(num)
    print(ans)
