def convert(text):
    words = text.split()
    words = set(words)
    words = sorted(words)
    result = " ".join(words)
    return result

x = "apple banana apple orange banana mango"
print(convert(x))
