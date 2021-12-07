# lambda x,y: x + y

f = lambda x, y: x + y

print(f(2, 3))

print("Wynik:", (lambda x, y: x + y)(3, 4))


def funkcja(f, liczba):
    return f(liczba)


# def dodaj(x):
#     return x + 1
#
#
# def kwadrat(parametr):
#     return parametr * parametr


# print(funkcja(dodaj, 7))
print(funkcja(lambda x: x + 1, 7))
# print(funkcja(kwadrat, 7))
print(funkcja(lambda x: x * x, 7))

lista = [1, 3, 5, 7]

print(f"Przykład z map: {list(map(lambda x: x * 2, lista))}")
print(f"Przykład z filter: {list(filter(lambda x: x > 3, lista))}")
