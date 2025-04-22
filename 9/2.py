def compute(n):
    a = str(n)
    b = a + a
    c = a + a + a
    d = a + a + a + a
    total = int(a) + int(b) + int(c) + int(d)
    return total

x = input("Enter a digit: ")
print(compute(x))