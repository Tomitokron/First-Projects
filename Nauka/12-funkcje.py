countries_information = {}
countries_information["Polska"] = ("Warszawa", 40.01)
countries_information["Niemcy"] = ("Berlin", 84.05)
countries_information["Węgry"] = ("Budapeszt", 23.02)

# Funkcja
def show_country_info(country):
    country_information = countries_information.get(country)

    print()
    print(country)
    print("------------")
    print("Stolica:" + country_information[0])
    print("Liczba mieszkańców (mln):" + str(country_information[1]))

for country in countries_information.keys():
    print(country)

country = input("Informację o jakim kraju chcesz wiedzieć?")

country_information = countries_information.get(country)
show_country_info(country)

# Funkcja, tylko do wyświetlania
def display_sum(a, b):
    print(a+b)

sum = display_sum(2, 6)
print(sum)

# Funkcja, która zwraca wartość
def calculate_sum(a, b):
    return a + b

sum = calculate_sum(2, 3)
print(sum)    

# W funkcji nic nie musimy wpisywać, aby coś wyświetlić
def print_message():
    print("Wiadomość testowa")
