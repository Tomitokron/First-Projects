from tkinter import N


name = "Tomasz"

print(len(name))
# len sprawdza długość znaków w zadeklarowanej zmiennej

print(name.capitalize())
# capitalize powoduje, że pierwsza litera zamienia się na duża literę
print(name.upper())
# upper powoduje, że wszystkie małe litery zamieniają się ma duże litery
print(name.lower())
# lower powoduje, że wszystkie duże litery zamieniają się na małe litery

print(name[0])
# Wyświetlanie litery wykonujemy za pomocą indeksów, czyli nawiasów kwadratowych
print (name[3:4])
# Wyświetla nam litery od 3 do 4
print(name[4:])
# Wyświelta nam litery od 4 do końca
print(name[-4:1])
# Wyświetli nam litery od 4 w dół, liczenie będzie w przeciwna stornę

channel = "Jak zacząć dobrze programować"
print(channel.split(" "))
# split pozwala na rozbicie słów
# w nawiasie po split'cie definujemy czym chcemy rozdzielić

join_string = "-"
print(join_string.join(['Jak', 'nauczyć']))

print(name.startswith("T")) # TRUE
print(name.startswith("l")) # FALSE
# Sprawdza czy nasza zmienna zaczyna od konkretnej litery

print(name.endswith("z")) # TRUE
print(name.endswith("g")) # FALSE
# Sprawdza czy nasza zmienna kończy od konkretnej litery

print(name.rstrip("z"))
# Usuwa litere po prawej stronie
print(name.lstrip("T"))
# Usuwa litera po lewej stornie
print(name.strip())
# Usuwa nadmierne spacje zarowno, z lewej jak i prawej storny

# Stringi można oczywiście łączyć

first_name = "Tomasz"
last_name = "Szurma"

print(first_name + " " + last_name)

# zfill dodaje nam zera przed tym co chcemy wyświetlić