def index_of_min(values):
    if len(values) == 0:
        return -1
    min_val = min(values)
    res = values.index(min_val)
    return res

if __name__ == '__main__':
    user_input = input("Введите элементы списка через пробел:")
    if user_input.strip() == "":
        my_list = []
    else:
        my_list = [float(x) for x in user_input.split()]

    ans = index_of_min(my_list)
    print(f"Индекс мнимального элемента: {ans}")
