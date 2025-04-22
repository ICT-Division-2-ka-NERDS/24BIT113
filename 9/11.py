def create_list(a, b):
    result = []
    for x in a:
        if x in b:
            result.append(x)
    return result

x = [1, 2, 3, 4]
y = [3, 4, 5, 6]
print(create_list(x, y))
