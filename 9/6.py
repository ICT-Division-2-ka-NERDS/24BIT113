def clean_list(a):
    if len(a) == 0:
        return []
    if a[0] < 0:
        return [0] + clean_list(a[1:])
    else:
        return [a[0]] + clean_list(a[1:])

x = [-1, 2, -3, 4, -5]
print(clean_list(x))
