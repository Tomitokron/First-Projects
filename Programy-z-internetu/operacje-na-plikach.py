plik = open("test.txt", "w")
print("Witaj nieznajomy. Wprowadź swoje dane, abyśmy wiedzieli jak się nazywasz")
if plik.writable():
    plik.write(input("Imię: ") + "\n")
    plik.write(input("Nazwisko: ") + "\n")
    plik.write(input("Nazwa użytkownika: ") + "\n")
    plik.write(int(input("Podaj swój wiek: ") + "\n"))
plik.close()

plik = open("test.txt", "r")

if plik.readable():
    tekst = plik.read()
    print("To są Twoje dane")
    print(tekst)