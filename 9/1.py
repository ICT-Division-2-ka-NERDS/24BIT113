def count_lower_upper(text):
    small = 0
    big = 0
    for letter in text:
        if letter.islower():
            small = small + 1
        elif letter.isupper():
            big = big + 1
    result = {'lower': small, 'upper': big}
    return result

a = "IaMJAYgAjjaR"
b = count_lower_upper(a)
print(b)
