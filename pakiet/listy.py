# imie = "Marek"
# user = ["Tomek", 323, 54.76, None, True, imie]
# lista2 = list()
# lista3 = ["Jarek", 352, 84.76]
# print(type(user))
# lista4 = user + lista3
# lista5 = [lista3,user]
# print(lista4)
# print(lista5)
import math

lista_cyfr = ["pierwszy", "drugi", "trzeci", "czwarty", "piąty"]
# print(lista_cyfr[0])
# print(lista_cyfr[-1])
# print(lista_cyfr[:-1])
# print(lista_cyfr[:3])
# lista_cyfr[0] = 1
# lista_cyfr[1:3] = [2, 3]

# lista_cyfr.append("szósty")
# lista_cyfr.insert(1, "Tomek")
# lista_cyfr.pop(1)
# lista_cyfr.remove("szósty")
# lista_cyfr.reverse()
# print(lista_cyfr)
# print(lista_cyfr)
# lista_cyfr2 = [456, 48, 45, 22, 11, 44, 9999, -55, 55]
# lista_cyfr2.sort()
# print(lista_cyfr2)
# print(min(lista_cyfr2))
# print(max(lista_cyfr2))
# print(428 in lista_cyfr2)
# print(len(lista_cyfr2))

listaW = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(listaW)
# print(listaW[2][0])  # [] - tabela [] - indeks w tej tabeli

kody = ("Tomek", 323, 54.76, None, True)
# print(math.pi)

slownik = {"jeden": 1,
           "drugi": 2,
           "trzeci": 3}

slownik1 = dict([("jeden", 1), ("drugi", 2), ("tzecia", 3)])

slow = {}
slow[(1, 2, 3)] = ("a", "b", "c")
print(slow)

# print(slownik)
# print("drugi" in slownik1)
# print(slownik.keys())
# print(slownik.values())
# print(slownik.items())
# slownik['czwarty'] = 4
# print(slownik)
print(slownik.get(89))
