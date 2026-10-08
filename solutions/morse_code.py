from morse import morse

def morse_code(text):
    text = text.upper()
    result = []
    
    for letter in text:
        if letter == " ":
            result.append(" ")
        else:
            result.append(morse[letter] + " ")
            
    return "".join(result).strip()

if __name__ == '__main__':
    print(to_morse("PYTHON 3"))
    print(to_morse("SOS"))
    print(from_morse('.--. -.-- - .... --- -. / ...--'))
    print(from_morse('... --- ...'))
