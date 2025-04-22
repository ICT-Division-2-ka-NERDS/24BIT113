def create_array(x, y, z, val):
    a = []
    for i in range(x):
        b = []
        for j in range(y):
            c = []
            for k in range(z):
                c.append(val)
            b.append(c)
        a.append(b)
    return a

r = create_array(2, 2, 2, 1)
print(r)
