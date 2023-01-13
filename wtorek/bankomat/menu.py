from bankomat import Bankomat


def menu():

    kasa = Bankomat(50, 200)

    while True:
        print('Wybierz operację: ')
        print('+ - wpłata: ')
        print('- - wypłata: ')
        print('* - sprawdzenie stanu konta: ')
        print('q - wyjście: ')

        oper = input("Twój wybór: ")

        if oper == 'q':
            print('Do zobaczenia')
            break

        elif oper == '+':
            ile = input("Podaj kwotę lub przerwij (q): ")
            if ile == 'q':
                print('Do zobaczenia')
                break
            print(f'Wykonujesz operację {get_pretty_name(oper)}: na kwotę {ile}')
            kasa.wplata(int(ile))

        elif oper == '-':
            ile = input("Podaj kwotę lub przerwij (q): ")
            if ile == 'q':
                print('Do zobaczenia')
                break
            print(f'Wykonujesz operację {get_pretty_name(oper)}: na kwotę {ile}')
            kasa.wyplata(int(ile))

        elif oper == '*':
            print(f'Wykonujesz operację {get_pretty_name(oper)}')
            kasa.stan()

        else:
            continue


def get_pretty_name(operation) -> str:
    if operation == "+":
        return "wpłaty"
    elif operation == "-":
        return "wypłaty"
    elif operation == "*":
        return "sprawdzenia konta"
