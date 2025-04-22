def prime_factors(n, i=2):
    if n == 1:
        return []
    if n % i == 0:
        return [i] + prime_factors(n // i, i)
    else:
        return prime_factors(n, i + 1)

x = int(input("Enter a number: "))
print(prime_factors(x))
