zmienna = 1
zmienna2 = "Abc"

lista = [1, 2, "c", "b", 1]
#        0, 1,  2,   3
print(lista)
print(lista[0])
print(lista * 3)

print()

tekst = "Hello"
print(tekst[1])

print("Ilośc elementów", len(tekst)) # len sprawdza ilość elementów

lista.append("f")
lista.append("a")

print(lista)
print()

lista.append(["f", "1"])
print(lista)

print()
print(lista[6][0]) # Odwołuje się do konkretnego indexu w liste, która została wpisana w inna listę

lista.insert(3, 3)
print(lista)
print()

print("Ilość:", lista.count(1)) # Zlicza ile jest wartości w naszej liscie
print("Index:", lista.index(3)) # Sprawdza index danej wartości

print()
lista.remove("f")
print(lista)

print()
print()

lista2 = [1, 5, 10, 20, 30]
print("Min:", min(lista2))
print("Max:", max(lista2))

print()

lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)
lista2.clear()
print(lista2)