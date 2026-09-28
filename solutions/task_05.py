def greet(username):
    res = f"Hello, {username}"
    return res

if __name__ == '__main__':
    name = input("Enter username: ")
    ans = greet(name)
    print(ans)
    
