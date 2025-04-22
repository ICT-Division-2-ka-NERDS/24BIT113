def ispangram(text):
    s = set(text.lower())
    a = set('abcdefghijklmnopqrstuvwxyz')
    if a<= s:
        return True
    else:
        return False

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("Crazy Fredrick bought many very exquisite opal jewels"))
