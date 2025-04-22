def count_alpha_digits(text):
    a = 0
    d = 0
    for ch in text:
        if ch.isalpha():
            a = a + 1
        elif ch.isdigit():
            d = d + 1
    return {'alphabets': a, 'digits': d}

x = "abc123xyz456"
print(count_alpha_digits(x))
