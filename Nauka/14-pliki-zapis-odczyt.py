file = open("country_and_capitals.txt", "w+")

for country, capitals in country_and_capitals.items():
    file.write() 

file.close()

###

file.open()

for line in file.readline():
    print(line.strip())

file.close()