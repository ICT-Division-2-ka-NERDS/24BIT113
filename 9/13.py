def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)

x = int(input("Enter a number: "))
b = to_binary(x)
if b == "":
    b = "0"
print(b)
