napis = "AAA BBB ..."
print(len(napis)) # 11
# Funkcja len() informuje nas z jak wielu znaków składa się napis. Zliczane są również spacje i znaki przestankowe.

napis = "abcdeabcde"
print(napis.index("a")) # 0
print(napis.index("d")) # 3
# Metoda index zwraca numer pierwszego znaku identycznego z tym podanym w nawiasie. Znaki numerowane są od lewej i od zera, tak samo jak tablicach.

napis = "abrakadabra"
print(napis.count("a"))  # 5
print(napis.count("ab")) # 2
# Ta metoda sprawdza ile razy w napisie pojawia się znak lub ciąg ujęty w cudzysłów.

napis = "abcdefghijk"
print(napis[2]) # c
# Za pomocą nawiasów kwadratowych możemy uzyskać dostęp do pojedynczego znaku, jeśli znamy jego indeks.