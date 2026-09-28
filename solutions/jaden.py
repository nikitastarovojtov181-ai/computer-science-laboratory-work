def to_jaden_case(text):
    words = text.split()

    jaden_words = [word.capitalize() for word in words]
    return " ".join(jaden_words)

if __name__ == '__main__':
    user_text = input("Введите строку: ")
    result = to_jaden_case(user_text)
    print("Результат: ")
    print(result)
