def index_of_min(values):
    if len(values) == 0:
        return -1
    min_val = min(values)
    res = values.index(min_val)
    return res

if __name__ == '__main__':
    user_input = input().strip()
    if user_input == "":
        my_list = []
    else:
        my_list = []
        for x in user_input.split():
            val = float(x) if '.' in x else int(x)
            my_list.append(val)

    ans = index_of_min(my_list)
    print(ans)
