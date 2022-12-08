
# print("Witaj w moim programie :D")

# print("Mam na imię Tomasz, a jak ty się nazywasz?")

# name = input("Podaj swoje imię: ")
# print = ("Nazywam się" + name)

# print("Masz ochotę zagrać ze mną w grę? ")

# tak = input("Tak mam ochęte zgrać w twoja gre ")
# nie = input("Nie, dzięki")

# if tak == 1:
#     print("Ekstra!")
# else:
#     print("Szkoda")



# a = 5
# b = 10 

# if a < b:
#     print(a + b)
# else:
#     print("Nie poprawna wartość")

# a = float(input("Podaj pierwszą liczbę: "))
# b = float(input("Podaj drógą liczbę: "))   

# print(a + b)

# x = True
# y = False

# if x == y:
#     print("To nie jest prawda")
# else:
#     print()

# print(5 == 6) # False

wiek = 16
kasa = 26000

if wiek >= 18 and kasa >= 2500:
    print("Możesz zacząć kurs prawa jazdy")
elif wiek < 18 and kasa < 2500:
    print("Jesteś za młody i masz za mało pieniędzy")
elif kasa < 2500:
    print("Masz nie wystarczającą ilość pieniędzy")
elif wiek < 18:
    print("Jesteś za młody na prawo jazdy")
else:
    print("Wpisane wartości są nie poprawne")