def funkcja(x):
    return x * x

wynik = funkcja
print(wynik(10))

def funkcja2(f1, x):
    return f1(x) * x

print(funkcja2(funkcja, 5))

## Rekurencja wewnątrz funkcji

def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)

print(silnia(5))


# silnia z !3 = 3 * 2 * 1 = 6