def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

x = int(input("Enter base: "))
y = int(input("Enter power: "))
print(power(x, y))
