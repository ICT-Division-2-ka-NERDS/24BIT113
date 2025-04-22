def total(a):
    if len(a) == 0:
        return 0
    return a[0] + total(a[1:])

def avg_list(a):
    if len(a) == 0:
        return 0
    return total(a) / len(a)

x = [10, 20, 30, 40, 50]
print(avg_list(x))
