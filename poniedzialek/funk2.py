from collections.abc import Sequence


def sum_numeric(limit = 10) -> int:
    s = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            s += n
    return s

def suma(seq: Sequence[int]) -> int:
    if len(seq) == 0:
        return 0
    return seq[0] + suma(seq[1:])

wyniki = []
wyniki.append(sum_numeric(20))
wyniki.append(sum_numeric(21))
wyniki.append(sum_numeric(22))
wyniki.sort()
print(wyniki)
print(suma(wyniki))
print(suma([2,3]))
print(suma([]))