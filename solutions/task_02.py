def bytes_to_kilobytes(value):
    res = value / 1024
    return res
def kilobytes_to_bytes(value):
    res = value * 1024
    return res

if __name__ == '__main__':
    val = float(input("Enter value: "))
    print("Choose direction: ")
    print("1: Bytes to kilobytes")
    print("2: Kilobytes to Bytes")
    choice = input("Your choice (1 or 2): ")

    if choice == "1":
        ans = bytes_to_kilobytes(val)
        print(f"Result: {ans}")
    elif choice == "2":
        ans = kilobytes_to_bytes(val)
        print(f"Result: {int(ans)}")
    else:
        print("Incorrect choice!")
