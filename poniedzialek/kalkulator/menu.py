from poniedzialek.kalkulator.calc import get_calculation


def menu():
    while True:
        print('Podaj działanie: ')
        print('+ - dodawanie: ')
        print('- - odejmowanie: ')
        print('* - mnożenie: ')
        print('/ - dzielenie: ')
        print('q - wyjście: ')

        f_calc = input("Działanie: ")



        if f_calc == 'q':
            break

        a = input("Liczba A: ")
        if a == 'q':
            break

        b = input("Liczba B: ")
        if a == 'q':
            break

        print(f'Wykonujesz operację {get_pretty_name(f_calc)}: {a} {f_calc} {b}')
        print(f'Twój wynik to: {get_calculation(f_calc, int(a), int(b))}')


def get_pretty_name(operation) -> str:
    if operation == "+":
        return "dodawania"
    elif operation == "-":
        return "odejmowania"
    elif operation == "*":
        return "mnożenia"
    elif operation == "/":
        return "dzielenia"