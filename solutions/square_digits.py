def square_digits(n):
    s = str(n)
    
    squared_parts = []
    
    for char in s:
        sq = str(int(char) ** 2)
        squared_parts.append(sq)
        
    result_str = "".join(squared_parts)
    
    return int(result_str)


if __name__ == '__main__':
    num = int(input("Введите число n: "))
    ans = square_digits(num)
    print(f"Результат склейки квадратов: {ans}")
