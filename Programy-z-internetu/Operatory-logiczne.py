# Operatory logiczne and i or (pol. "i" i "lub") pozwalają na budowanie kompletnych zdań logicznych, na przykład:

imie = "Jan"
wiek = 23
if imie == "Jan" and wiek == 23:
    print("Nazywasz sie Jan i masz 23 lata.")

if imie == "Jan" or imie == "Robert":
    print("Nazywasz sie Jan lub Robert")

# Za pomocą operatora "in" możesz sprawdzić, czy konkretny obiekt znajduje sie w tablicy lub innym obiekcie gromadzącym inne obiekty:

imie = "Robert"
if imie in ["Jan", "Robert"]:
    print("Nazywasz sie Jan lub Robert")


#Operator "is"
#W przeciwieństwie do ==, operator is nie sprawdza, czy zmienne mają taką samą wartość, ale czy wskazują na ten sam obszar w pamięci komputera. Na przykład:

x = [1,2,3]
y = [1,2,3]
print(x) == y # Wypisze True
print(x) is y # Wypisze False

tablica = [1, 2, 3]
tablica2 = ['a', 'b', tablica]
print(tablica == tablica2[2]) # True
print(tablica is tablica2[2]) # True

# Ponizej dowod na to, ze is mowi prawde

tablica.append(4) # Dodajemy do tablicy liczbe 4
print(tablica2[2]) # [1, 2, 3, 4]

# Operator "not"
# Używając not przed wyrażeniem logicznym zmieniamy jego wartość na przeciwną:

print(not False)           # Wypisze True
print(not False) == (False) # Wypisze False