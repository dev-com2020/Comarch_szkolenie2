import pliki


liczby = list(range(1, 10, 2))
print("Wygenerowana lista: ", liczby)

imiona = ['Jakub', 'Bartosz', 'Julia', 'Max', 'Agata']
usun = int(input("Podaj który usunąć: "))
imiona.pop(usun)
print(imiona)



# for i in liczby:
#     print(i)

# index = 0
# while index < len(liczby):
#     print("liczby[", index, "] -> ", liczby[index], sep="")
#     index += 1

# for index, wartosc in enumerate(liczby):
#     print(str(index)+" -> "+str(wartosc))
#
# licznik = 0
# while True:
#     licznik += 1
#     print(licznik)
#     if licznik == 10:
#         break

# lista = []
# print('Podaj liczby całkowite, wpisz "stop" aby zakończyć')
# while True:
#     wejscie = input(":\n")
#     if wejscie == 'stop':
#         break
#     lista.append(int(wejscie))
# print('Twoja lista: ->', lista)


