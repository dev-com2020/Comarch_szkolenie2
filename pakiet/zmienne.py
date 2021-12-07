# imie = 'Tomek'
# ulubionyJezyk = "Python"
# wiek = -38888888888888888
# wzrost = 1.7689765398573098574390574
# czyPali = False
# czy_lata = None

# print(help(wiek))
# print(type(czyPali))
# print(type(imie))
# print(type(wiek))
# print("Typem wieku jest:", type(wzrost))
# print(type(czy_lata))

# '''
# Tutaj
# komentarz
# blokowy
# '''
#
# x = 5 + 2 - 3.43 * 3
# y = 5 / 2
# z = 5 // 2
# v = 5 % 2
# b1 = 2 ** 8

# print("Wynik:", float(v))

# a = int(input("Wpisz liczbę a:"))
# b = int(input("Wpisz liczbę b:"))
# print('Wynik= >', a > b)
# print('Wynik= <=', a <= b)
# print('Wynik= ==', a == b) # is jest tym samym
# print('Wynik= !=', a != b)

# prawda = True
# falsz = False
#
# print(prawda and falsz) # &
# print(prawda or falsz) # |
# print(not prawda)

# print('wynik:', x, "\nA tu może \tbyć \"inny\" wynik")
#
# print(f'''
#        wynik:, {x}, A tu może być inny wynik   A tutaj jeszcze inny tekst
#        wynik:, x, A tu może być inny wynik     A tutaj jeszcze inny tekst
#        wynik:, x, A tu może być inny wynik     A tutaj jeszcze inny tekst
# ''')
#
# print("Tu 'jeszcze' inny tekst", end=" ")
# print("Tu jeszcze inny tekst", end=" ")
# print("Tu jeszcze \"inny\" tekst")

# imie = 'Tomek'
# print(imie[0])
# print(imie[-1])
# print(len(imie))
# print(imie[2:3])
# print(imie[2:])
# print(imie[2:4])
# print(imie[:2])
# print(imie.count("t"))
# print("Tutaj jakiś napis".count(" "))

w = 3.86
# print("Używamy Pythona w wersji:", w)
# print("Używamy Pythona w wersji: %i" % w)
# print("Używamy Pythona w wersji: %.f" % w)
# print("Używamy Pythona w wersji: %.1f" % w)
# print("Używamy Pythona w wersji: %.2f" % w)
# print("Używamy Pythona w wersji: %.3f" % w)
#
# print(f"Używamy Pythona w wersji: {w}")
#
# j1, j2 = "Pyton", "Java"

# print("Moim ulubionym językiem jest", j1, "oraz", j2)
# #print(f"Używamy Pythona w wersji: {j2}")
# print("Używamy Pythona w wersji: %s" % j1)

print("Moim ulubionym językiem jest %(jezyk)" % {"jezyk": "Python"})
