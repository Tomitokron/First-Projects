from cgi import print_directory


x = 10
y = 0

try:
    print(x / y)
    print("Linijka po")
except ZeroDivisionError:
    print("Nastąpiło dzielenie przez 0!")
except TypeError:
    print("Błąd typów modułów")
except:
    print("Inny bląd!")
finally:
    print("Wykonam się i tak")

z = int(input("Podaj liczbę: "))
c = int(input("Podaj drugą liczbę: "))

if z == c:
    print(z, "jest równe", c)
elif z > c:
    print(z, "jest większe od", c)
elif c < z:
    print(c, "jest mniejsze od", z)
else:
    print("Podane wartości są błędne") 