oceny = {5, 2, 1, 3, 4, 6, 3, 2}
temp = {36.6, 39.4, 37.8}
klasa = ["Marek", "Janek", "Anna", "Janek", "Tomek"]
klasaB = {"Marek", "Janek", "Anna", "Janek"}
inne_oceny = set(klasa)
print(inne_oceny - klasaB)
print(inne_oceny.difference(klasaB))
print(inne_oceny.intersection(klasaB))
print(inne_oceny & klasaB)
print(inne_oceny | klasaB)

# print(oceny)
# print(inne_oceny)
# print(temp)
