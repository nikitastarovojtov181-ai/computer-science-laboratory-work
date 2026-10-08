import math

def is_strong(n):
    total_sum = 0
    
    for digit in str(n):
        total_sum += math.factorial(int(digit))
        
    return total_sum == n

if __name__ == '__main__':
    print(is_strong(1))
    print(is_strong(2))
    print(is_strong(145))
    print(is_strong(123))
