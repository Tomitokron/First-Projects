# [ Test Type 
name = "Tomasz"         #Aby przejść do następnej linijki, nie używamy entera, tylko \n.
name = 'Tomasz\'Szurma' #Używając zmienej '', aby przedłużyć dalszy ciąg tekstu, trzeba użyć pomiędzy \. Tak jak zostało to zrobione w przykładzie.
name = """Tomasz"""     #Tutaj nie trzeba użwyać komendy \n, a enter zostanie zdefiniowany poprawnie

print (name)

#Są to trzy sposoby na zainicjowanie stinga, czyli [str]
# ]

# [Numeric Types]
a = 20
b = 4.56

print (a + b)
print (a + b * a)

a = 1_000_000.01
print(a)

# [Type Bool] Logiczny (Przyjmuje wartości True albo False)

is_sky_blue = True
is_sun_blue = False

print(is_sky_blue)
print(is_sun_blue)

print(type(name))
print(type(a))
print(type(is_sky_blue))

# W pythonie nie da się dodac dwóch typów, dlatego robi się type(zmienna)

first = 2
second = "4"

print(first + int(second))

# Jest to konwersja. Konwersja typów musi mieć SENS!