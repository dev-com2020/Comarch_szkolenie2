import random


def wygrane(szostka, lista):
    wynik = 0
    for i in lista:
        if i in szostka:
            wynik += 1
    return wynik


random.seed()

# setup
liczby = []
n = 100000  # liczba losowań
kupon = 3
trojka = 24
czworka = 264
piatka = 7150
szostka = 10000000

for i in range(6):
    wybrane = int(input("Podaj sześć liczb:"))
    liczby.append(wybrane)

wins = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

for i in range(n):
    losowanie = sorted(random.sample(range(1, 50), 6))
    wyniki = wygrane(liczby, losowanie)
    print("Wylosowano liczby {}. Trafiłeś {}".format(losowanie, wyniki))
    wins[wyniki] += 1

inwest = n * kupon
wygrana = wins[3] * trojka + wins[4] * czworka + wins[5] * piatka + wins[6] * szostka
print("^" * 30)
print("Podsumowanie:")
print("Zera: {}\nJedynki:{}\nDwójki:{}\nTrójki:{}\nCzwórki:{}\nPiątki:{}\nSzóstki:{}\n".format(wins[0],
                                                                                   wins[1],
                                                                                   wins[2],
                                                                                   wins[3],
                                                                                   wins[4],
                                                                                   wins[5],
                                                                                   wins[6]))
print("^" * 30)
print("Zainwestowałeś: {} złotych, a wygrałeś {} złotych. Twój bilans to {} zł.".format(inwest,
                                                                                        wygrana, wygrana - inwest))
