import sys
import random
import string

password = []
characters_left = -1

def update_characters_left(number_of_charecters):
    global characters_left

    if number_of_charecters < 0 or number_of_charecters > characters_left:
        print("Liczba znaków spoza przedziału 0,", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_charecters
        print("Pozostało znaków:", characters_left)

passwod_length = int(input("Jak długie ma być hasło? "))

if passwod_length < 5:
    print("Hasło musi mieć minimum 5 znaków, spróbuj jeszcze raz.")
    sys.exit(0)
else:
    characters_left = passwod_length

lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))
update_characters_left(lowercase_letters)

uppercase_letters = int(input("Ile dużych liter ma mieć hasło? "))
update_characters_left(uppercase_letters)

special_characters = int(input("Ile znaków specialnych ma mieć hasło? "))
update_characters_left(special_characters)

digits = int(input("Ile cyfr ma mieć hasło? "))
update_characters_left(digits)

if characters_left > 0:
    print("Nie wszystkie znaki zostały wykorzystne. Hasło zostanie uzupełnione małymi literami.")
    lowercase_letters += characters_left

print()
print("Długość hasła:", passwod_length)
print("Małe litery:", lowercase_letters)
print("Duże litery:", uppercase_letters)
print("Znaki specjalne:", special_characters)
print("Cyfry:", digits)

for _ in range(passwod_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Wygenerowane hasło:", "".join(password))