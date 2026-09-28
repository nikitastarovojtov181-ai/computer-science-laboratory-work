def echo_number(number):
    res = f"Thats the number you entered {number}"
    return res

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    ans = echo_number(num)
    print(ans)
