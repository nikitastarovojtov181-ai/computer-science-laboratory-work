def is_automorphic(n):
    square = n ** 2
    
    str_n = str(n)
    str_square = str(square)
    
    return str_square.endswith(str_n)

if __name__ == '__main__':
    print(is_automorphic(25))
    print(is_automorphic(76))
    print(is_automorphic(5))
    print(is_automorphic(13))
