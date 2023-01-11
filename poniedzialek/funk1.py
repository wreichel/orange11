def powitanie(imie:str):
    print(f"Witaj, {imie.title()} !")


def powitanie2(imie: str, wiek=18, *liczba):
    return f"Witaj, {imie.title()}, masz {wiek} lat. Magiczna liczba to {liczba} !"

powitanie("wojtek")
powitanie(str(123))
print(powitanie2("jarek"))


imie = powitanie2("jarek", 25, 5, 55, 22)

imiona = []
imiona.append(imie)
print(imiona)
