import pandas as pd

w = pd.read_excel('imiona.xlsx',sheet_name='Wynik2',header=None, names=['Imię', "Nazwisko", "Wynik"])
print(w)
w.to_csv('wyniki.csv')

# lista = [[1, 3, 5, 7], [2, 4, 6, 8]]
# z = pd.DataFrame(lista)
# z.columns = ['Pierwsza', 'Druga', "Trzecia", "Czwarta"]
# print(z)
#
# slownik = {'Imię': ['Ania', "Tomek", "Przemek"], 'Wiek': [18, 38, 25]}
# print(pd.DataFrame(slownik))

# zbior = pd.DataFrame()
# print(zbior)
