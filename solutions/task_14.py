def circle_diameter(radius):
    d = radius * 2
    return d

def sum_range(start, end):
    total = 0

    for i in range(start, end + 1):
        total = total + 1
    return total

if __name__ == '__main__':
    user_input_r = input()
    r = float(user_input_r) if '.' in user_inpit_r else int(user_input_r)
    
    s = int(input())
    e = int(input())
    
    ans_diameter = circle_diameter(r)
    ans_sum = sum_range(s, e)
    
    print(ans_diameter)
    print(ans_sum)
