import time


def drukuj(funkcja):
    def wew(*args, **kwargs):
        print("Udekorowałem :)")
        return funkcja(*args, **kwargs)

    return wew


@drukuj
def wyniki():
    time.sleep(2)
    print("Podaje wyniki.....")


@drukuj
def dodawanie(a, b):
    time.sleep(1)
    print("wynik=", a + b)

wyniki()
dodawanie(2, 2)
