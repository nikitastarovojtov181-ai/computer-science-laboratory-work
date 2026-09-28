def compare(m, n):
    if m > n:
        return "Number m > n"
    elif m < n:
        return "Number m < n"
    else:
        return "The number are equal"

if __name__ == '__main__':
    val1 = float(input("Enter m: "))
    val2 = float(input("Enter n: "))

    ans = compare(val1, val2)
    print(ans)
