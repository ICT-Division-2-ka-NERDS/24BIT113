def make_list(n):
    a = []
    for i in range(1, n+1):
        a.append((i, i*i, i*i*i))
    return a

print(make_list(5))
