country_and_capitals = {'Poland': 'Warsaw', 'Czechia': 'Praga'}

try:
    print(country_and_capitals['USA'])
except:
    print("Panstwo nie znalezione")
finally:
    print("To wykona sie zawsze")

print("Udało się")