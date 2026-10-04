def compare(m, n):
    if m > n:
        return "Number m > n"
    elif m < n:
        return "Number m < n"
    else:
        return "The numbers are equal"

if __name__ == '__main__':
    val1 = float(input())
    val2 = float(input())

    ans = compare(val1, val2)
    print(ans)
