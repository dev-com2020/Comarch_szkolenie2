

def f1():
    global a
    a = 1
    b = 2
    return a + b

def f2():
    c = 3
    return a + c

def drukuj():
    print("Wydrukowałem...")


def ksero(tekst, ile):
    return (tekst + " ") * ile


def dodaj(a, b):
    return a, b


def podziel(a, b=1):
    return a / b


def pomnoz(a: int, b: str):
    return a * b


def duzo_rzeczy(a="treść", b="coś innego", *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)