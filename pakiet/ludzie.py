class Human:
    '''
    Tutaj może być opis klasy, czyli jej metody, pola itd...
    '''

    def __init__(self, imie, wiek, plec):
        '''
        :param imie: tutaj podaj str
        :param wiek: tutaj podaj int
        :param plec: tutaj wpisz "m" lub "k"
        '''
        self.imie = imie
        self.wiek = int(wiek)
        self.plec = plec

    def przywitaj(self):
        '''
        :return: zwraca imię wprowadzone w konstruktor
        '''
        print("Cześć, mam na imię:", self.imie)

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")

    def mysl(self):
        if self.wiek < 2:
            print("Gugugaga...")
        else:
            print("6434+3423/323232")


t = Human("Tomek", 38, "m")

t.przywitaj()
t.ruszaj()
t.mysl()

a = Human("Ania", 25, "k")

a.przywitaj()
a.ruszaj()
a.mysl()

print(t.imie, t.wiek, t.plec)
