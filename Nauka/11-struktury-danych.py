# Lista imion
names_list =  [] # [], uzywamy gdy chcemy stworzyc pusta listę
names_list.append("Tomasz") #append dodaję nam wartości do naszej listy
names_list.append("Kuba")

# Inny sposób dodawania wartości do naszej listy. Możemy zrobic to od razu.
names_list = ["Andrzej", "Rafał"]

names_list.reverse() # Reverse powoduje odwrócenie

names_list.sort() # Sort powoduje posortowanie

print(names_list.count("Tomasz")) # Zlicza ile razy jest słowo Tomasz

print(names_list)
print(names_list[2]) # Wybieramy za pomocą indeksu, co chcemy aby się wyświetliło

# Krotka, używa ona nawiasów otwartych ( )
person = ("Tomasz", "Szurma")
print(person)

# Set, używa on nawiasow klamrowych {}
names_set = {"Tomasz", "Marisuz"}
names_set = set() # dodaje pustą liste
names_set.add("Kamil")
names_set.add("Andrzej")
 
# Dictionary używa {}
# W słowniku możemy do zapsiu państw  itp.

contries = {"Poland": "Warsaw", "Germany": "Berlin"}

print(contries)