# light = input("Jakie jest światlo? (red, green, yellow)")

# if light == 'red':
#     print ("Czekaj!")
# elif light == 'yellow':
#     print("Przygotuj się!")
# # elif, jest to sprawdzenie kolejnego warunku
# elif light == 'green':
#     print("Jedź!")
# else:
#     print("Niewłaściwa wartość")

jajko = input("Ile chcesz gotować jajko? (3 minuty, 5 minut, 15 minut)")

if jajko == '3 minuty':
    print("Jajko będzie surowe w środku")
elif jajko == '5 minut':
    print("Jajko będzie idealnie przygotowane")
elif jajko == '15 minut':
    print("Jajko będzie rozgotowane")
else:
    print("Wybrany czas gotowania jest nie poprawny")
 