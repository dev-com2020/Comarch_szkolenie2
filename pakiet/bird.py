from abc import ABC, abstractmethod


class Bird(ABC):
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "Startuje i osiągnę szybkość:", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Bird):

    def __init__(self, szybkosc):
        super().__init__("Orzeł", szybkosc)

    def poluj(self):
        print("Tu", self.gatunek, "Startuje i rozpoczynam polowanie")

    def wydajOdglos(self):
        print("Wrrrrrrr")


class Kura(Bird):

    def __init__(self):
        super().__init__("Kura", 0)

    def znoszeJajko(self):
        print("Tu", self.gatunek, "Właśnie znoszę jajko,kokoko")

    def lataj(self):
        print("Tu", self.gatunek, "Ja nie umiem latać!!!")

    def wydajOdglos(self):
        print("kokokok")


o = Orzel(80)
k = Kura()

o.lataj()
o.poluj()
k.znoszeJajko()
k.lataj()
k.wydajOdglos()
o.wydajOdglos()
