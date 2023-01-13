class Bankomat:

    def __init__(self, limit_wy: int, limit_wp: int):
        '''
        :param limit_wy: Limit wypłat
        :param limit_wp: Limit wpłat
        '''
        self.__stan = 100
        self.limit_wy = limit_wy
        self.limit_wp = limit_wp

    def wplata(self, ile):
        if ile > self.limit_wp:
            self.limit('wpłaty', self.limit_wp)
        else:
            self.__stan += ile
        self.stan()

    def wyplata(self, ile):
        if ile > self.limit_wy:
            self.limit('wypłaty', self.limit_wy)
        elif ile > self.__stan:
            self.nomoney()
        else:
            self.__stan -= ile
        self.stan()

    def stan(self):
        print(f'Twój stan konta wynosi {self.__stan}')

    def limit(self, oper, ile):
        print(self, f'Twój limit dla operacji {oper} wynosi {ile}')

    def nomoney(self):
        print(self, f'Brak wystarczającej ilości środków \n'
                    f'Podaj kwotę mniejszą od {self.__stan}')
