number = 1

while number <= 6:
    print(number)
    number += 2

# Pętla WHLIE będzie się wykonywac do momentu, kiedy nie zostanie spełniony odpowiedni warunek

for  number in range (1 ,10, 2): # 2 w tym przypadku liczy co dwa
    print(number)

for  number in range (1 ,10):
    if number == 5:
        break # Powoduje zatrzymanie się pętli w wyznaczonym przez nas miejscu
        continue # Powoduje przerwanie dotychczasowej pętli i rozpoczyna od miejsca wyznaczonego przez nas
    print(number)

# Pętla FOR będzie wykonywać się w odpowiednim zakresie
