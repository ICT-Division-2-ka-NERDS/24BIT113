def frequency(text):
    words = text.split()
    words = sorted(words)
    result = {}
    for w in words:
        if w in result:
            result[w] = result[w] + 1
        else:
            result[w] = 1
    return result

x = "apple orange apple banana apple mango banana"
print(frequency(x))
