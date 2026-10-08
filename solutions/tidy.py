def is_tidy(n):
    s = str(n)
    
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
            
    return True

if __name__ == '__main__':
    print(is_tidy(12))
    print(is_tidy(32))
    print(is_tidy(13779))
    print(is_tidy(2335))
    print(is_tidy(7))
